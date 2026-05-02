
---

# 📑 Resumo Usuários e Grupos no Linux

## 🗄️ 1. Arquivos Fundamentais do Sistema

|**Arquivo**|**Localização**|**Propósito**|**Sensibilidade**|
|---|---|---|---|
|👤 **passwd**|`/etc/passwd`|Atributos públicos (UID, Shell, Home).|🟢 Baixa (Leitura global)|
|👤 **shadow**|`/etc/shadow`|Hashes de senhas e políticas de expiração.|🔴 **Altíssima** (Root)|
|👥 **group**|`/etc/group`|Define grupos e lista seus membros.|🟢 Baixa (Leitura global)|
|👥 **gshadow**|`/etc/gshadow`|Versão segura do `group` (senhas de grupos).|🟡 Alta (Root)|

---

## 🛠️ 2. Estrutura e Delimitação (`:`)

### 📂 Arquivo `/etc/passwd`

**Sintaxe:** `nome:senha:UID:GID:Gecos:diretório_home:shell`

|**Campo**|**Descrição**|**Detalhes Técnicos**|
|---|---|---|
|**1. Nome**|Login único|Ex: `euriandes`|
|**2. Senha**|Indicador `x`|Senha real armazenada no `/etc/shadow`|
|**3. UID**|User ID|**0** sempre será o Root|
|**4. GID**|Group ID|ID do Grupo Primário do usuário|
|**5. Gecos**|Comentário|Informações extras (Nome Real, Contato)|
|**6. Home**|Home Path|Ex: `/home/usuario`|
|**7. Shell**|Interpretador|Ex: `/bin/bash` ou `/usr/bin/zsh`|

> [!ABSTRACT] **Significado do Campo de Senha (x)**
> 
> - `x`: **Shadowed** (Padrão moderno: senha no `/etc/shadow`).
>     
> - `!`: **Locked** (Conta bloqueada via `passwd -l`).
>     
> - `*`: **Disabled** (Conta de serviço, sem login interativo).
>     
> - `!!`: **New Account** (Criada, mas sem senha definida).
>     
> - `*NP*`: **No Password** (Ambientes NIS).
>     
> - `$`: **Hash Identifier** (Início de um hash estruturado no shadow).
>     

---

### 🔐 Arquivo `/etc/shadow`

**Sintaxe:** `usuario:hash:ultima_alteracao:min:max:aviso:inativo:expira:reservado`

#### 🧬 Tabela de Algoritmos (Identificador de Hash)

|**ID**|**Algoritmo**|**Nível**|**Observação Sênior**|
|---|---|---|---|
|`$1$`|**MD5**|🔴 Obsoleto|Vulnerável a ataques de colisão.|
|`$2a$`|**Blowfish**|🟡 Seguro|Comum em BSD; propositalmente lento.|
|`$5$`|**SHA-256**|🟡 Seguro|Sólido, mas vulnerável a aceleração por GPU.|
|`$6$`|**SHA-512**|🟢 Alto|Padrão robusto da indústria (RHEL/Ubuntu).|
|`$y$`|**Yescrypt**|🛡️ **Elite**|**Padrão no Arch Linux**; resistente a GPUs (Memory-hard).|

---

### 👥 Arquivo `/etc/group`

**Sintaxe:** `nome_do_grupo:senha:GID:lista_de_usuarios`

#### 🛡️ Grupos de Sistema e Segurança (Audit)

|**Grupo**|**Finalidade**|**Risco/Contexto**|
|---|---|---|
|**root**|Superusuário|Controle total e irrestrito.|
|**wheel/sudo**|Adm (RBAC)|Permite elevar privilégios via `sudo`.|
|**docker**|Virtualização|**Risco Crítico:** Equivalente a root.|
|**www-data**|Web Server|Isolamento de processos Apache/Nginx.|
|**wireshark**|Segurança|Permite _sniffing_ sem privilégios de root.|
|**systemd-journal**|Logs|Permite leitura do `journalctl` por users.|

---

## ⌨️ 3. Comandos de Manipulação

> [!WARNING] **Atenção**
> 
> A edição direta manual destes arquivos é desencorajada. Utilize os binários específicos para garantir a integridade da sintaxe.

### ➕ 1. `useradd` (Criação)

_Comando de baixo nível para novos registros._

- `-m`: Cria o diretório Home.
    
- `-s`: Define o Shell padrão.
    
- `-g`: Define o GID principal.
    
- `-c`: Adiciona comentário (Gecos).

	![[useradd -h.png]]

### 📝 2. `usermod` (Modificação)

_Edita valores sem corromper a estrutura do arquivo._

- `-l`: Altera o nome de login.
    
- `-d -m`: Altera o Home e move os arquivos fisicamente.
    
- `-L` / `-U`: Trava (Lock) e Destrava (Unlock) a conta.
    
	![[usermod_command.png.png]]
### ❌ 3. `userdel` (Remoção)

_Remove a linha nos arquivos `/etc/passwd` e `/etc/shadow`._

- **Sem flags:** Remove o usuário, mas **mantém** os arquivos no disco.
    
- `-r`: (Recursive) Deleta o Home e o spool de e-mail. **(Limpeza total)**.
    

### 🔑 4. `passwd` (Gestão de Senhas)

_Foca primordialmente nas políticas do `/etc/shadow`._

- `-e`: Força troca de senha no próximo login.
    
- `-x`: Define validade máxima da senha.
    
- `-d`: Remove a senha do usuário (Não recomendado para admin).
    

---

## 🔍 4. Ferramentas de Auditoria e Integridade

|**Comando**|**Função**|**Por que usar?**|
|---|---|---|
|`id`|Verificação|Valida UID/GID e grupos suplementares ativos.|
|`getent`|Consulta|Busca em arquivos locais ou rede (LDAP/AD).|
|`pwck`|**Integridade**|Verifica erros de sintaxe ou campos ausentes.|
|`chsh`|Shell|Altera o campo 7 de forma interativa.|

---

### 💡 Conceitos de Nível Baixo (Glossário)

- **Shadowing:** Técnica de segurança que separa dados públicos (passwd) de segredos criptográficos (shadow).
    
- **RBAC (Role-Based Access Control):** Controle de acesso baseado em funções (ex: grupo `wheel`).
    
- **Memory-hard:** Algoritmos (como Yescrypt) que exigem RAM, impedindo que hackers usem milhares de núcleos de GPU para quebrar sua senha.