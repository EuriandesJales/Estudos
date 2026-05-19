Aqui está o resumo técnico e estruturado do incidente, ideal para o seu conhecimento e para documentação no seu cofre do **Obsidian**.

---

# 📝 Post-Mortem Técnico: Falha de Permissão OCI no Distrobox (Rootless Podman)

## 1. O Sintoma (O Erro)

Ao tentar iniciar um contêiner através do comando `distrobox enter lab-ubuntu`, o processo falhava com a seguinte mensagem de erro de baixo nível:

Plaintext

```
runc: runc create failed: unable to start container process: error during container init: 
error mounting "/dev/vboxusb/001/003" to rootfs at "/dev/vboxusb/001/003": 
openat2 /dev/vboxusb/001/003: permission denied: OCI permission denied
```

---

## 2. Análise de Causa Raiz (O "Porquê")

O problema ocorreu devido a um conflito de arquitetura entre o isolamento de segurança de contêineres **rootless (sem root)** e o gerenciamento de permissões de hardware do host.

1. **Ação do Distrobox:** Para garantir a máxima integração com o host, o Distrobox tenta realizar um _bind mount_ (mapeamento direto) de todos os dispositivos encontrados em `/dev` do host para dentro do contêiner. Isso inclui os nós de dispositivos USB do VirtualBox (`/dev/vboxusb/...`).
    
2. **O Bloqueio do Kernel (Namespaces):** Contêineres rootless usam **User Namespaces** do kernel Linux. O seu usuário pertence ao grupo `vboxusers` no host, o que te dá acesso ao VirtualBox. Porém, por motivos de segurança, o runtime padrão **`runc`** descarta os grupos suplementares do usuário do host ao criar o sandbox do contêiner.
    
3. **A Syscall Falha (`openat2`):** Quando o `runc` tentou criar o ponto de montagem usando a chamada de sistema moderna `openat2`, o kernel barrou a operação com `permission denied`. O runtime não tinha a identidade do grupo `vboxusers` dentro do namespace do contêiner para abrir o arquivo especial de dispositivo.
    

> 💡 **Por que alterar as permissões do VirtualBox no host não seria a solução ideal?**
> 
> Mudar as permissões em `/dev` (via `chmod`) seria uma "gambiarra" temporária. Ela quebraria o princípio de privilégio mínimo, exporia o hardware de forma insegura e seria desfeita automaticamente pelo gerenciador de pacotes do Arch na próxima atualização do VirtualBox.

---

## 3. O Passo a Passo da Solução

A estratégia adotada foi substituir o runtime de contêiner de baixo nível do Go (`runc`) por uma implementação em C mais moderna (`crun`), que possui suporte nativo para preservação segura de grupos suplementares.

### Passo 1: Instalação do runtime `crun`

Instalamos o binário otimizado diretamente dos repositórios oficiais do Arch Linux.

Bash

```
sudo pacman -Syu crun
```

### Passo 2: Configuração do Podman no Escopo do Usuário

Criamos/editamos o arquivo de configuração do Podman em formato **TOML** dentro da pasta do usuário (`~/.config/containers/containers.conf`), definindo o `crun` como padrão e mapeando explicitamente seus caminhos absolutos:

Ini, TOML

```
[engine]
runtime = "crun"

[engine.runtimes]
crun = [
    "/usr/bin/crun",
    "/usr/local/bin/crun"
]
```

### Passo 3: Limpeza de Estado e Sincronização do Storage

Forçamos o Podman a derrubar processos em segundo plano (`conmon`) e atualizar os metadados do armazenamento do contêiner para aplicar a nova configuração:

Bash

```
podman system migrate
```

### Passo 4: Recriação do Contêiner do Distrobox

Como o contêiner antigo foi criado sob as regras do `runc`, os metadados antigos estavam persistidos no storage local. Forçamos a recriação do contêiner para que ele nascesse sob a nova gerência do `crun`:

Bash

```
distrobox rm lab-ubuntu --force
distrobox create --name lab-ubuntu --image ubuntu:latest
distrobox enter lab-ubuntu
```

---

## 4. A Lógica da Solução (Por que funcionou?)

A substituição para o **`crun`** resolveu o problema de forma elegante na camada da aplicação (Enterprise Ready) sem tocar em nenhuma permissão global do sistema host:

- **Manipulação Avançada de Syscalls:** O `crun` é capaz de utilizar a chamada de sistema `setgroups()` em conjunto com os recursos modernos do kernel Linux para fazer o _pass-through_ (passagem direta) dos grupos suplementares do seu usuário do host de forma segura.
    
- **Respeito às Flags:** Ele interpreta corretamente as diretivas do Distrobox (como `--group-add keep-groups`). Quando o contêiner tentou montar o `/dev/vboxusb`, o `crun` provou ao kernel que o processo rootless tinha o GID do `vboxusers` associado legitimamente no host, permitindo a montagem e iniciando o shell do Ubuntu com sucesso.
    

---

### 📚 Glossário Técnico para Documentação

- **OCI (Open Container Initiative):** Conselho que padroniza os formatos de imagem e runtimes de contêineres na indústria Linux.
    
- **runc / crun:** Motores de baixo nível responsáveis por receber a imagem do contêiner do Podman/Docker e interagir com o Kernel (namespaces e cgroups) para dar vida ao processo isolado.
    
- **User Namespaces:** Recurso do Kernel Linux que permite mapear UIDs/GIDs de dentro de um contêiner para UIDs/GIDs diferentes no host, base fundamental de contêineres rootless.