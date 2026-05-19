
O **LunarVim (lvim)** é uma IDE baseada em Neovim que adota uma filosofia _leader-centric_ e orientada a plugins modernos (como o _Which-Key_). Compreender seus atalhos exige entender que a maioria das ações globais é mapeada a partir da tecla **Leader** (que por padrão no LunarVim é o `Space` / Barra de Espaço).

Abaixo está um resumo técnico e estruturado dos principais atalhos, organizados por contexto operacional, ideal para consolidar sua _cheat sheet_ no Obsidian.

---

## 1. A Tecla Leader (`Space`) e Navegação Global

O componente `Which-Key` entra em ação assim que você pressiona `Space`. Se você hesitar por alguns milissegundos, um menu visual será aberto no rodapé mostrando as próximas opções.

|**Atalho**|**Ação**|**Contexto/Explicação**|
|---|---|---|
|`Space` + `f`|**Find File**|Abre o _Telescope_ para busca rápida de arquivos por nome (Fuzzy Finding).|
|`Space` + `st`|**Search Text**|Busca global por string de texto no projeto (utiliza o `ripgrep` por baixo dos panos).|
|`Space` + `e`|**Toggle Explorer**|Abre/Fecha a árvore de arquivos lateral (_Nvim-Tree_).|
|`Space` + `c`|**Close Buffer**|Fecha o buffer atual sem quebrar o layout das janelas (_windows_).|
|`Space` + `q`|**Quit**|Fecha o LunarVim (solicita salvamento se houver alterações).|
|`Space` + `w`|**Save**|Atalho rápido para salvar o buffer atual (`:w`).|

---

## 2. Gerenciamento de Buffers e Janelas (Splits)

No ecossistema Vim/Neovim, entender a diferença entre _Buffers_ (arquivos carregados em memória) e _Windows_ (as divisões visuais na tela) é fundamental.

### Buffers (Abas superiores no Lvim)

- **`Shift` + `l` (ou `]` + `b`)**: Move para o **próximo** buffer da direita.
    
- **`Shift` + `h` (or `[` + `b`)**: Move para o buffer **anterior** da esquerda.
    

### Windows (Divisões de Tela / Splits)

O LunarVim herda os atalhos nativos do Neovim para navegação entre splits usando a tecla `Ctrl`, eliminando a necessidade de usar `Ctrl + w` seguido da direção.

- **`Ctrl` + `h`**: Move o foco para a janela da **esquerda**.
    
- **`Ctrl` + `j`**: Move o foco para a janela de **baixo**.
    
- **`Ctrl` + `k`**: Move o foco para a janela de **cima**.
    
- **`Ctrl` + `l`**: Move o foco para a janela da **direita**.
    

---

## 3. LSP (Language Server Protocol) e Intellisense

Como o LunarVim é voltado para desenvolvimento moderno, a integração com o LSP nativo do Neovim é um dos seus pontos mais fortes. Os atalhos abaixo são válidos quando o cursor está sobre um símbolo (variável, função, classe).

|**Atalho**|**Ação**|**Arquitetura / O que acontece por baixo**|
|---|---|---|
|`g` + `d`|**Go to Definition**|Salta diretamente para onde o símbolo foi definido.|
|`g` + `r`|**Go to References**|Abre o Telescope listando todas as ocorrências do símbolo no projeto.|
|`K`|**Hover Doc**|Abre um _floating window_ com a documentação/assinatura do método.|
|`Space` + `la`|**Code Actions**|Sugere correções rápidas do LSP (ex: importar módulo ausente).|
|`Space` + `lr`|**Rename**|Renomeia o símbolo e todas as suas referências de forma segura no projeto.|
|`Space` + `ld`|**Diagnostics**|Abre a lista de erros/warnings do arquivo atual através do _Trouble_ ou Telescope.|

---

## 4. Integração com Git (Gitsigns & LazyGit)

O LunarVim utiliza o plugin `gitsigns.nvim` para monitoramento de _hunks_ (trechos de código modificados) diretamente no _gutter_ (coluna ao lado dos números das linhas).

- **`Space` + `gg`**: Abre o **LazyGit** (uma interface de terminal extremamente poderosa para Git, se instalada no sistema).
    
- **`]` + `g`**: Salta para o **próximo** hunk modificado.
    
- **`[` + `g`**: Salta para o hunk modificado **anterior**.
    
- **`Space` + `gj`**: Próxima modificação (alternativo).
    
- **`Space` + `gk`**: Modificação anterior (alternativo).
    
- **`Space` + `gl`**: Abre o _Git Blame_ na linha atual de forma flutuante.
    
- **`Space` + `gd`**: Abre um _Git Diff_ visual do arquivo atual contra o commit mais recente.
    

---

## 5. Terminal Integrado (`ToggleTerm`)

Para evitar a quebra de contexto saindo do editor para rodar comandos ou scripts Python/Docker:

- **`Ctrl` + `\`**: Abre/Oculta o terminal integrado flutuante (ou horizontal/vertical, dependendo da sua config).
    
- **`Esc` `Esc`** (dentro do terminal): Entra no modo normal do Vim dentro do terminal, permitindo navegar pelo output e copiar textos.
    

---

### Dica Prática de Produtividade:

Se você esquecer um atalho específico de um menu (como o menu de LSP ou de Busca), basta apertar `Space` e aguardar 1 segundo. O menu inferior guiará você pelas subcategorias (ex: `l` para LSP, `s` para Search, `g` para Git).

## 🚀 Os Essenciais do Shell (Terminal)

### Movimentação e Edição Rápida

- **`Ctrl` + `a`** / **`Ctrl` + `e`** : Vai direto para o **Início** / **Fim** da linha.
    
- **`Ctrl` + `u`** / **`Ctrl` + `w`** : Apaga a linha **inteira** / Apaga apenas a **última palavra**.
    

### Histórico e Fluxo

- **`Ctrl` + `r`** : Busca inteligente no histórico de comandos (digite o termo para buscar).
    
- **`Alt` + `.`** : Cola o **último argumento** do comando anterior (ex: se usou `mkdir pasta`, digite `cd` e use o atalho).
    
- **`Ctrl` + `l`** : Limpa a tela instantaneamente.
    

### Controle de Processos

- **`Ctrl` + `c`** : Interrompe e **mata** o comando/processo atual.
    
- **`Ctrl` + `z`** : **Pausa** o processo e joga para o background (digite `fg` para voltar).
    

---

## 🌙 Os Essenciais do LunarVim (`lvim`)

_A maioria começa com a barra de espaço (`Space`)._

### Arquivos e Navegação

- **`Space` + `f`** : Busca arquivos pelo nome no projeto (_Fuzzy Finder_).
    
- **`Space` + `st`** : Busca por um texto/palavra dentro de qualquer arquivo do projeto.
    
- **`Space` + `e`** : Abre/fecha a barra lateral de arquivos.
    
- **`Space` + `w`** / **`Space` + `c`** : **Salva** o arquivo / **Fecha** a aba atual (_buffer_).
    

### Movimentação entre Janelas (Splits)

- **`Ctrl` + `h` / `j` / `k` / `l`** : Move o cursor entre as telas divididas (**Esquerda / Baixo / Cima / Direita**).
    
- **`Shift` + `h`** / **`Shift` + `l`** : Alterna entre as abas abertas no topo.
    

### Código e LSP

- **`g` + `d`** : Vai direto para a **definição** da função/variável sob o cursor.
    
- **`K`** (Shift+k) : Mostra a documentação/assinatura da função em uma janela flutuante.
    
- **`Space` + `lr`** : Renomeia a variável em todo o projeto de uma vez só.