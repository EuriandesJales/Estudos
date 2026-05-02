# 🛡️ Flatseal: Gestão de Sandbox e Hardening de Aplicações

O **Flatseal** é uma ferramenta gráfica baseada em GTK que permite revisar e modificar as permissões de aplicativos **Flatpak**. Ele atua como um editor visual para os _overrides_ (substituições) de permissão que, de outra forma, teriam que ser feitos via CLI.

## 🏗️ Como Funciona (Arquitetura)

O Flatseal manipula os metadados do **Bubblewrap** (o utilitário de sandboxing que o Flatpak usa). Quando você altera uma chave no Flatseal, ele gera um arquivo de configuração em `~/.local/share/flatpak/overrides/`, que o runtime do Flatpak lê antes de iniciar a aplicação.

### Áreas de Controle:

- **Namespaces:** Isola rede, IPC e processos.
    
- **XDG Portals:** Define como o app interage com o sistema de arquivos via "buracos" controlados.
    
- **D-Bus:** Controla a comunicação entre processos no sistema.
    

## 🚀 Instalação e Configuração

No Arch Linux, você pode instalar a versão oficial via Flathub (recomendado para manter o isolamento da própria ferramenta).

```
# Adicionar repositório Flathub (se não tiver)
flatpak remote-add --if-not-exists flathub [https://flathub.org/repo/flathub.flatpakrepo](https://flathub.org/repo/flathub.flatpakrepo)

# Instalar Flatseal
flatpak install flathub com.github.tchx84.Flatseal
```

## 🛠️ Como Usar (Workflow de Segurança)

Para um perfil de **SecInfo**, o uso deve seguir o fluxo de **Deny by Default** (Negar por padrão):

### 1. Seleção e Revisão

Ao abrir o Flatseal, a coluna da esquerda lista seus apps. A coluna da direita mostra as permissões atuais divididas por categorias.

### 2. Categorias Críticas para Auditoria:

|Categoria|Função|Recomendação de Segurança|
|---|---|---|
|**Share**|Rede (Network) e IPC.|Desative `network` se o app for offline (ex: calculadoras).|
|**Socket**|Conexão com Wayland/X11.|Prefira `wayland` e desative `x11` para evitar keyloggers.|
|**Device**|GPU, Som, Webcam.|Desative `multimedia` se não precisar de câmera/microfone.|
|**Filesystem**|Acesso a pastas do sistema.|Desative `home` e `host`. Use apenas pastas específicas.|
|**Environment**|Variáveis de sistema.|Cuidado com chaves de API expostas em variáveis `$ENV`.|

### 3. Reset de Emergência

Se um app parar de funcionar após você restringir demais:

- Clique no botão **"Reset"** no topo superior direito para voltar às configurações padrão do desenvolvedor.
    


> [!TIP] **Segurança no X11 vs Wayland** Aplicativos X11 podem, tecnicamente, ler inputs de outros aplicativos. No Flatseal, se você usa Wayland, desative o socket `x11` e mantenha apenas `fallback-x11` ou `wayland` para garantir que o app não espione seu teclado.

> [!IMPORTANT] **Persistent Storage** Se você desativar o acesso ao sistema de arquivos (`Filesystem`), o app ainda pode salvar dados em `~/.var/app/ID_DO_APP`. Isso é o armazenamento isolado (per-app) que não afeta o resto do seu sistema.

## ⌨️ Atalhos úteis via CLI (Equivalentes ao Flatseal)

Se precisar automatizar via script Python ou Bash:

- **Listar overrides:** `flatpak override --show com.exemplo.App`
    
- **Remover acesso à rede:** `flatpak override --nosocket=network com.exemplo.App`
    
- **Resetar tudo:** `flatpak override --reset com.exemplo.App`