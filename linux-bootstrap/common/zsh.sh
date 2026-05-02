#!/usr/bin/env bash

# Este  script esta em produçao
# NAO EXECUTE ELE O MESMO PODE QUEBRAR O SEU SO


set -euo pipefail

echo "[+] Instalando dependências..."
sudo pacman -S --needed zsh git curl

echo "[+] Definindo Zsh como shell padrão..."
if [[ "$SHELL" != *"zsh" ]]; then
  chsh -s /bin/zsh
fi

echo "[+] Criando estrutura de diretórios..."
ZSH_DIR="$HOME/.config/zsh"
PLUGINS_DIR="$ZSH_DIR/plugins"
THEMES_DIR="$ZSH_DIR/themes"

mkdir -p "$PLUGINS_DIR" "$THEMES_DIR"

echo "[+] Instalando plugins..."

# Autosuggestions
if [[ ! -d "$PLUGINS_DIR/zsh-autosuggestions" ]]; then
  git clone https://github.com/zsh-users/zsh-autosuggestions \
    "$PLUGINS_DIR/zsh-autosuggestions"
fi

# Syntax Highlighting
if [[ ! -d "$PLUGINS_DIR/zsh-syntax-highlighting" ]]; then
  git clone https://github.com/zsh-users/zsh-syntax-highlighting \
    "$PLUGINS_DIR/zsh-syntax-highlighting"
fi

# Completions
if [[ ! -d "$PLUGINS_DIR/zsh-completions" ]]; then
  git clone https://github.com/zsh-users/zsh-completions \
    "$PLUGINS_DIR/zsh-completions"
fi

echo "[+] Instalando Powerlevel10k..."
if [[ ! -d "$THEMES_DIR/powerlevel10k" ]]; then
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
    "$THEMES_DIR/powerlevel10k"
fi

echo "[+] Gerando configuração .zshrc..."

cat > "$HOME/.zshrc" << 'EOF'
# ================================
# ZSH CONFIG - MINIMAL PROFISSIONAL
# ================================

# Paths
ZSH_CONFIG="$HOME/.config/zsh"
ZSH_PLUGINS="$ZSH_CONFIG/plugins"
ZSH_THEMES="$ZSH_CONFIG/themes"

# Completion system
autoload -Uz compinit
compinit

# Melhor UI de autocomplete
zstyle ':completion:*' menu select

# Plugins
source $ZSH_PLUGINS/zsh-autosuggestions/zsh-autosuggestions.zsh

fpath=($ZSH_PLUGINS/zsh-completions/src $fpath)

# Syntax highlighting (SEMPRE por último)
source $ZSH_PLUGINS/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Tema
source $ZSH_THEMES/powerlevel10k/powerlevel10k.zsh-theme

# History tuning
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history

setopt appendhistory
setopt sharehistory
setopt hist_ignore_all_dups

# Autosuggestions tuning
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#555"

# Aliases úteis
alias ll='ls -lah'
alias la='ls -A'
alias l='ls -CF'
EOF

echo "[+] Setup concluído!"

echo
echo "⚠️ IMPORTANTE:"
echo "1. Reinicie o shell ou rode: exec zsh"
echo "2. Rode: p10k configure"
echo "3. Quando perguntar sobre ícones, responda: NO"
