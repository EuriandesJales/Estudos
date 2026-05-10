#!/usr/bin/env bash
# ==============================================================================
# Dev Workflow Setup — Debian/Ubuntu
# Instala e configura: Zsh + plugins, Powerlevel10k, Kitty, Tmux, LunarVim,
# Neofetch e todas as dependências necessárias.
#
# Fluxo final: Kitty abre → Tmux inicia automaticamente → cada painel usa Zsh
# ==============================================================================
# 0.2
# AVISO NAO EXECUTE

set -euo pipefail


# ── Cores para output ──────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # Sem cor (reset)

# ── Funções de log ─────────────────────────────────────────────────────────────
log()       { echo -e "${GREEN}[✔ INFO]${NC}  $1"; }
warn()      { echo -e "${YELLOW}[⚠ AVISO]${NC} $1"; }
erro()      { echo -e "${RED}[✘ ERRO]${NC}  $1"; exit 1; }
titulo()    { echo -e "\n${BOLD}${BLUE}══════════════════════════════════════════${NC}"; \
              echo -e "${BOLD}${BLUE}  ► $1${NC}"; \
              echo -e "${BOLD}${BLUE}══════════════════════════════════════════${NC}"; }
subtitulo() { echo -e "\n${CYAN}  ┌─ $1${NC}"; }



# ------------------------------------------------------------------------------
# Verificações iniciais
# ------------------------------------------------------------------------------
verificar_sistema() {
    titulo "Verificando sistema"

    if ! command -v apt &>/dev/null; then
        erro "Este script requer apt (Debian/Ubuntu). Sistema não suportado."
    fi

    if [ "$EUID" -eq 0 ]; then
        erro "Não execute este script como root. Use seu usuário normal com sudo."
    fi

    log "Sistema: $(. /etc/os-release && echo "$PRETTY_NAME")"
    log "Usuário: $USER"
}

# ------------------------------------------------------------------------------
# Dependências base do sistema

dependencias_base=(
        # Ferramentas essenciais
        "git"               # Suporte ao git
        "curl"              # Cliente HTTP
        "wget"              # Baixador de arquivos
        "unzip"             # Descompactador de arquivos
        "tar"               # Empacotador de arquivos
        "make"              # Gerador de build
        "build-essential"   # Ferramentas de desenvolvimento
        "pkg-config"        # Necessário para que o compilador encontre as bibliotecas instaladas no sistema durante o build.
        
        # Gerenciador de projetos
        "cargo"             # Gerenciador de pacotes Rust
        "uv"                # Gerenciador de pacotes universal (uv.sh)
        "cargo"             # Gerenciador de pacotes Rust
        #"npm"               # Gerenciador de pacotes Node.js

        # ── Shell e terminal 
        "zsh"               # Terminal zsh
        "fontconfig"        # Configuração de fontes
        "fastfetch"         # Informações do sistema
        "tmux"              # Terminal multiplexer
        "ripgrep"           # Buscador de texto
        "fd-find"           # Localizador de arquivos
        "fzf"               # Selecionador de opções
        "ranger"            # Gerenciador de arquivos no terminal
        "tldr"              # Resumos de comandos no terminal
        "ipython"           # Shell interativo para Python

         # ── Ferramentas de desenvolvimento Compiladores
        "luarocks"          # Gerenciador de pacotes Lua
        "cmake"             # Gerador de build
         #"gcc"               # Compilador C

        # ── Linguagens de programação
        "python3-full"      # Python 3 com todos os módulos
        "python3"           # Python 3
        "python3-pip"       # Gerenciador de pacotes Python 3
        "pyenv"             # Gerenciador de versões Python
        "pipx"              # Gerenciador de pacotes Python 3
        "python3-pynvim"    # Bindings de Python para NVim
        "rustc"             # Compilador Rust
       
        # ── Docker e contêineres
        "docker.io"         # Docker Engine
        "docker-compose"    # Docker Compose

        # ── VM
        "virtualbox"        # VirtualBox para máquinas virtuais
        

        # ── Ferramentas de produtividade

        # ── Redes e Segurança
        "nmap"              # Scanner de rede
        "wireshark"         # Analisador de pacotes de rede
        #"shellcheck"    # Analisador de scripts shell
        "metasploit"         # O framework principal
        "postgresql"         # Banco de dados necessário para a base do MSF
        "netcat"

        # ── IDES e editores
       "micro"              # Editor de texto Micro
        #"neovim"            # Editor de texto Neovim
        #"lunarvim"          # Configuração do Neovim otimizada para desenvolvimento
        #"visual-studio-code" # Editor de código Visual Studio Code

        # ── Utilitários adicionais
        #"xclip"             # Copiador de texto
             
)

Install_() {
    titulo "Instalando conjunto de softwares"
    for pkg in "${dependencias_base[@]}"; do
        sudo pacman -S --noconfirm --needed "$pkg" || erro "Falha ao instalar $pkg"
        log "Instalado: $pkg"
    done
    
    log "Todas as dependências base foram instaladas."
}


# ------------------------------------------------------------------------------
# Nerd Fonts — MesloLGS NF (necessária para Powerlevel10k e ícones do LunarVim)
# ------------------------------------------------------------------------------
instalar_fontes() {
    titulo "Instalando Nerd Fonts (MesloLGS NF)"

    local FONT_DIR="$HOME/.local/share/fonts/MesloLGS"
    mkdir -p "$FONT_DIR"

    local BASE_URL="https://github.com/romkatv/powerlevel10k-media/raw/master"
    local FONTS=(
        "MesloLGS%20NF%20Regular.ttf"
        "MesloLGS%20NF%20Bold.ttf"
        "MesloLGS%20NF%20Italic.ttf"
        "MesloLGS%20NF%20Bold%20Italic.ttf"
    )

    for fonte in "${FONTS[@]}"; do
        local nome
        nome=$(echo "$fonte" | sed 's/%20/ /g')
        if [ ! -f "$FONT_DIR/$nome" ]; then
            wget -q -O "$FONT_DIR/$nome" "$BASE_URL/$fonte"
            log "Baixada: $nome"
        else
            warn "Já existe: $nome"
        fi
    done

    # Atualizar cache de fontes do sistema
    fc-cache -fv &>/dev/null
    log "Cache de fontes atualizado."
}

# ------------------------------------------------------------------------------
# Plugins Zsh + Powerlevel10k
# Todos clonados em ~/.zsh/plugins para organização
# ------------------------------------------------------------------------------
instalar_plugins_zsh() {
    titulo "Instalando plugins do Zsh"

    local PLUGIN_DIR="$HOME/.zsh/plugins"
    mkdir -p "$PLUGIN_DIR"

    declare -A PLUGINS=(
        ["zsh-autosuggestions"]="https://github.com/zsh-users/zsh-autosuggestions"
        ["zsh-syntax-highlighting"]="https://github.com/zsh-users/zsh-syntax-highlighting"
        ["zsh-completions"]="https://github.com/zsh-users/zsh-completions"
        ["zsh-history-substring-search"]="https://github.com/zsh-users/zsh-history-substring-search"
        ["gitstatus"]="https://github.com/romkatv/gitstatus.git"
        ["powerlevel10k"]="https://github.com/romkatv/powerlevel10k.git"
    )

    for nome in "${!PLUGINS[@]}"; do
        if [ -d "$PLUGIN_DIR/$nome" ]; then
            warn "Plugin '$nome' já existe. Atualizando..."
            git -C "$PLUGIN_DIR/$nome" pull --quiet
        else
            log "Clonando $nome..."
            git clone --depth=1 "${PLUGINS[$nome]}" "$PLUGIN_DIR/$nome"
        fi
    done

    log "Todos os plugins instalados."
}

# ------------------------------------------------------------------------------
# LunarVim
# Instala via script oficial. Depende de: nvim, node, npm, pip3, cargo (rust)
# ------------------------------------------------------------------------------
instalar_rust() {
    if ! command -v cargo &>/dev/null; then
        log "Instalando Rust (necessário para LunarVim)..."
        curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --quiet
        # shellcheck source=/dev/null
        source "$HOME/.cargo/env"
        log "Rust instalado."
    else
        warn "Rust já instalado. Pulando."
    fi
}

instalar_lunarvim() {
    titulo "Instalando Neovim"

    
    titulo "Instalando LunarVim"

    instalar_rust

    if command -v lvim &>/dev/null; then
        warn "LunarVim já instalado. Pulando."
        return
    fi

    log "Iniciando instalador oficial (contornando PEP 668)..."
    
    # Exportamos a variável para que todos os processos filhos do bash vejam
    export PIP_BREAK_SYSTEM_PACKAGES=1
    
    LV_BRANCH='release-1.3/neovim-0.9' \
        bash <(curl -s https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.3/neovim-0.9/utils/installer/install.sh) --yes
    
    # Desativa após a instalação por segurança
    unset PIP_BREAK_SYSTEM_PACKAGES
}

 ------------------------------------------------------------------------------
# Alterar shell padrão para Zsh (caso ainda não tenha sido feito)
# ------------------------------------------------------------------------------
definir_zsh_padrao() {
    titulo "Definindo Zsh como shell padrão"

    local ZSH_PATH
    ZSH_PATH=$(which zsh)

    # Adicionar zsh à lista de shells válidos se não estiver
    if ! grep -q "$ZSH_PATH" /etc/shells; then
        echo "$ZSH_PATH" | sudo tee -a /etc/shells
    fi

    if [ "$SHELL" != "$ZSH_PATH" ]; then
        chsh -s "$ZSH_PATH"
        log "Shell alterado para $ZSH_PATH. Faça logout/login para aplicar."
    else
        warn "Zsh já é o shell padrão."
    fi
}

# ------------------------------------------------------------------------------
# Mensagem final com próximos passos
# ------------------------------------------------------------------------------
mensagem_final() {
    titulo "Setup Concluído!"

    echo -e "${GREEN}"
    echo "  ✔ Dependências base instaladas"
    echo "  ✔ Neovim (AppImage) instalado"
    echo "  ✔ Fontes MesloLGS NF instaladas"
    echo "  ✔ Plugins Zsh instalados"
    echo "  ✔ LunarVim instalado"
    #echo "  ✔ Tmux configurado (.tmux.conf)"                      #Wip
    #echo "  ✔ Kitty configurado (inicia Tmux automaticamente)"    #Wip
    echo -e "${NC}"
    echo -e "${YELLOW}Próximos passos:${NC}"
    echo "  1. Faça logout e login novamente (ou rode: exec zsh)"
    echo "  2. Abra o Kitty — o Tmux iniciará automaticamente"
    echo "  3. Configure o tema: p10k configure"
    echo "  4. Configure a fonte do seu emulador para: MesloLGS NF"

}


# ------------------------------------------------------------------------------
# MAIN — Execução em ordem
# ------------------------------------------------------------------------------
main() {
    verificar_sistema
    Install_
    instalar_fontes
    instalar_plugins_zsh
    instalar_lunarvim
    definir_zsh_padrao
    mensagem_final
}

main
