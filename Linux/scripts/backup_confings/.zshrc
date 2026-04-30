# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="powerlevel10k/powerlevel10k"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
#requisitos pra plugin de tab autocompletar
autoload -Uz compinit
compinit -d ~/.zcompdump


plugins=(git
	colored-man-pages	#deixa mauais coloridos
	sudo						# Rescreve comando com sup quando da erro vc não é sudo
	#copydir					#copia o diretorio atual para a variavel copydir
	copybuffer					# copia o comando digitado para a area de transferencia
	dirhistory					# precione alt lefth para voltar alt right para desfazer retorno
	history						# Pesquisa por comando no historico hsi comando
	web-search					# Pesquisa no google com o comando google
	alias-finder				# recomenda alias para comandos muito usados
	#dotevn						# carrega envs automaticamene ao entrar diretorio de projeto com env
	zsh-autosuggestions
	zsh-syntax-highlighting
	zsh-completions
	)

source $ZSH/oh-my-zsh.sh
# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='nvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch $(uname -m)"
###---------------HISTORICO----------------------###
HISTSIZE=100000
SAVEHIST=10000
setopt HIST_IGNORE_ALL_DUPS       # remove duplicatas
setopt HIST_REDUCE_BLANKS         # remove espaços em branco
setopt SHARE_HISTORY              # compartilha histórico entre sessões


###---------------------------ALIAS--------------------------###
alias src="source ~/.zshrc" # recarrega zsh

###--------------------------FUNC----------------------------###
#copia o diretorio atual
copydir() { 
  pwd | xclip -selection clipboard
}

# Busca no ChatGPT Free (abre navegador)
gptweb() {
  local query="${*}"
  xdg-open "https://chat.openai.com/?q=$(echo $query | sed 's/ /%20/g')"
}

# busca por erros e aviso em arquivos (parametro 1=caminho/do/arquivo/nome.txt
erros_log() {
  local arquivo="$1" #Pega o primeiro argumento (o caminho do arquivo)

  if [[ -z "$arquivo" || ! -f "$arquivo" ]]; then #Verifica se o caminho é válido
    echo "Uso: erros_log /caminho/para/arquivo.log"
    return 1
  fi

   (
    # procura por string 'erro|warn'
    grep -iE 'erro|warn' "$arquivo" --color=always
    # ordena as linhas para o uniq funcionar corretamente
    sort
    # remove linhas duplicadas consecutivas
    uniq
  	) | less -R  # exibe com paginação e mantém cores
  
}

# RODA O TMUX
if command -v tmux &>/dev/null; then
	# Verifica se Não esta dentro de uma sessão de tmux
	if [[ -z "$TMUX" ]] && [[ -z "$ZSH_TMUX_AUTO" ]]; then
		export ZSH_TMUX_AUTO=1 # Flag para evitar loop
		exec tmux new-session -A -s default
	fi
fi

neofetch # pura e simples frescura

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux não está instalado!"
  return 1
fi

#if [[ -z "$TMUX" ]]; then
#  # Se não estiver no tmux, inicie o tmux
#  tmux
#fi


#neofetch
