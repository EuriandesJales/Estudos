
Aqui está um memorial descritivo completo e estruturado sobre toda a jornada de diagnóstico e engenharia reversa que realizamos até agora. Este documento foi formatado seguindo padrões corporativos, ideal para o seu cofre de documentação técnica no **Obsidian**.

---

# 📑 Relatório Técnico: Engenharia de Ambiente para Cisco Packet Tracer via Distrobox

## 1. Visão Geral do Projeto

O objetivo desta operação foi implantar o **Cisco Packet Tracer (v9.0.0)** de forma isolada, escalável e segura dentro do sistema operacional **Arch Linux (CachyOS)**. Em vez de utilizar máquinas virtuais pesadas ou poluír o sistema host com pacotes `.deb` convertidos incorretamente, adotamos o **Distrobox** com uma imagem base do **Ubuntu**, garantindo desempenho nativo de hardware.

---

## 2. A Linha do Tempo dos Problemas e Resoluções

### Fase 1: O Bloqueio OCI no Ambiente Rootless (Padrão)

- **Sintoma:** O comando `distrobox enter` falhava imediatamente com o erro:
    
    `openat2 /dev/vboxusb/001/003: permission denied: OCI permission denied`.
    
- **Causa Raiz:** O Distrobox tenta mapear todo o diretório `/dev` do host para o contêiner. O runtime padrão do Podman (`runc`) em modo _rootless_ (sem privilégios) descarta os grupos suplementares do usuário (como o grupo `vboxusers` do VirtualBox) por motivos de segurança. Ao tentar criar o ponto de montagem via chamada de sistema `openat2`, o kernel do Linux barrava a operação.
    
- **Solução Aplicada:**
    
    1. Instalamos e configuramos o runtime moderno **`crun`** no arquivo `~/.config/containers/containers.conf`. O `crun` possui suporte nativo à chamada `setgroups()`, permitindo passar os grupos suplementares do host de forma segura.
        
    2. Executamos `podman system migrate` e recriamos o contêiner para aplicar os novos metadados.
        

### Fase 2: O Conflito do AppImage e FUSE com a flag `--root`

- **Sintoma:** Ao rodar o Packet Tracer, o terminal acusava `mkdir: Permission denied` e travava em bibliotecas gráficas (`libOpenGL.so.0`).
    
- **Causa Raiz:** Descobrimos que a Cisco distribui o Packet Tracer em formato `.deb`, mas internamente o executável principal é encapsulado em um **AppImage** (`/opt/pt/packettracer.AppImage`). O AppImage necessita montar um sistema de arquivos virtual via **FUSE** em `/tmp`. No modo _rootless_, o kernel proíbe um usuário comum de realizar montagens complexas de hardware/FUSE dentro de namespaces isolados.
    
- **Solução Aplicada:** Recriamos o contêiner do Distrobox utilizando a flag estrita de sistema **`--root`** (`distrobox create --root --name lab-packttracer`). Isso vincula o motor do contêiner ao UID 0 (root real) do host, permitindo que o App Tracer herde as capacidades necessárias do kernel para gerenciar o FUSE e o barramento gráfico da GPU diretamente.
    

### Fase 3: O Travamento de Contas no Distrobox 1.8.2.5

- **Sintoma:** Após criar o contêiner como `--root`, o sistema pedia uma senha para o usuário que não era a do host, não era vazia e não era "ubuntu". A flag `--user` retornava erro.
    
- **Causa Raiz:** O Distrobox espelha o seu usuário para dentro do contêiner, mas o Linux proíbe a cópia direta de hashes de senhas cifradas do host para o arquivo `/etc/shadow` interno por segurança. O usuário nascia bloqueado. Além disso, a versão _bleeding-edge_ do Distrobox (1.8.2.5) possuía um bug de validação sintática na linha 69 do script ao lidar com o comando `sudo`.
    
- **Solução Aplicada:** Ignoramos as travas do script do Distrobox e injetamos um shell diretamente através do motor nativo com o comando:
    
    `sudo podman exec -it -u root lab-packttracer /bin/bash`.
    
    Uma vez logados como superusuário real, redefinimos a senha do usuário comum com o comando `passwd`.
    

### Fase 4: Depuração da "Cascata de Dependências" do Chromium

- **Sintoma:** O programa fechava em sequência acusando falta de bibliotecas `.so` específicas (`libnss3.so`, `libpulse.so.0`).
    
- **Causa Raiz:** O Packet Tracer 9.0 possui um motor web baseado em Chromium embutido para renderizar as telas de login da Cisco NetAcad. Imagens Docker/Podman minimalistas não trazem pacotes de interface ou multimídia por padrão.
    
- **Solução Aplicada:** Saneamos o ambiente instalando manualmente as bibliotecas de segurança, renderização e áudio ausentes via `apt`:
    
    - `libnss3` (Network Security Services da Mozilla / Engine Web).
        
    - `libpulse0` (Cliente PulseAudio para os efeitos sonoros de rede e VoIP).
        
    - Bibliotecas Mesa/X11 adjacentes (`libopengl0`, `libgbm1`, etc.).
        

---

## 3. Arquitetura Final: O "Porquê" Funciona

A lógica do estado atual do seu laboratório se resume a este fluxo de engenharia de sistemas:

```
[Seu Monitor/Teclado] 
      │
[Host: Arch Linux (CachyOS)] ──> Roda o Servidor Gráfico (Wayland/X11) e Som (PipeWire)
      │
      ├─> [Podman Daemon (Rootful / UID 0)] ──> Permite montagem FUSE do AppImage
            │
            └─> [Contêiner Ubuntu (Distrobox --root)]
                     │
                     ├─> Bibliotecas Gráficas/Som instaladas (NSS, OpenGL, Pulse)
                     │
                     └─> [Cisco Packet Tracer] ──(Pass-Through)──> Renderiza na tela do Arch
```

Ao rodar como `--root` e suprir as bibliotecas compartilhadas que o binário compilado dinamicamente exigia, permitimos que o ecossistema fechado da Cisco converse com o Kernel do seu Arch Linux sem violar os limites do sistema operacional principal.