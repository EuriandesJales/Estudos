#!/bin/bash
############################################################################################
# Faz uma copia de arquivos de configuração
############################################################################################
# Versao 1.0
# faz copia do zshrc tema p10k confs do gnome terminal

# Diretório onde o backup será salvo (data e hora no nome para versionar)
BACKUP_DIR="$HOME/backup_config_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "Backup será salvo em: $BACKUP_DIR"

# Backup dos arquivos de configuração do Zsh e Powerlevel10k
cp -v ~/.zshrc "$BACKUP_DIR/"
cp -v ~/.p10k.zsh "$BACKUP_DIR/"

# Exportar a paleta do GNOME Terminal via dconf
PROFILE_ID=$(dconf list /org/gnome/terminal/legacy/profiles:/ | grep '^:' | head -n1 | tr -d '/')

if [ -n "$PROFILE_ID" ]; then
  echo "Exportando paleta do GNOME Terminal do perfil $PROFILE_ID"
  dconf dump /org/gnome/terminal/legacy/profiles:/:$PROFILE_ID/ > "$BACKUP_DIR/gnome-terminal-profile-$PROFILE_ID.dconf"
else
  echo "Perfil do GNOME Terminal não encontrado, pulando exportação da paleta."
fi

echo "Backup concluído com sucesso."
