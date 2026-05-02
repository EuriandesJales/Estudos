
Este é um guia de referência rápida (Cheat Sheet) de Bash focado em sintaxe para quem já domina a lógica de programação. Estruturado para ser colado diretamente no seu **Obsidian**.

---

# 🌀 Bash Scripting: Syntax Reference Guide

## 1. Variáveis e Escopo
O Bash trata tudo como string por padrão. Não use espaços ao redor do operador `=`.

```bash
# Declaração
nome="Gemini"
readonly CONSTANTE="Valor Fixo"

# Referência (Sempre use aspas duplas para evitar Word Splitting)
echo "$nome"

# Comando para variável (Command Substitution)
data_atual=$(date +%Y-%m-%d)
```

## 2. Tipos de Dados: Arrays e Dicionários
Arrays no Bash são indexados (base 0). Dicionários (Associative Arrays) exigem declaração explícita.

### Arrays (Listas)
```bash
lista=("A" "B" "C")
lista+=("D")              # Append
echo "${lista[0]}"        # Acessar índice
echo "${lista[@]}"        # Todos os itens
echo "${#lista[@]}"       # Comprimento do array
```

### Dicionários (Maps)
```bash
declare -A config
config=( ["porta"]=8080 ["host"]="localhost" )
echo "${config["porta"]}"
```

## 3. Condicionais (if/else)
Use `[[ ... ]]` (testes estendidos) em vez de `[ ... ]` para maior segurança e recursos (como Regex).

```bash
if [[ "$var" == "valor" ]]; then
    # código
elif [[ "$var" =~ ^[0-9]+$ ]]; then # Regex
    # código
else
    # código
fi
```

### Operadores de Comparação
| Tipo | Operador |
| :--- | :--- |
| **String** | `==`, `!=`, `-z` (vazia), `-n` (não vazia) |
| **Inteiro** | `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge` |
| **Arquivo** | `-e` (existe), `-f` (é arquivo), `-d` (é diretório) |

## 4. Loops (Estruturas de Repetição)

### For Loop (Estilo Lista)
```bash
for item in "${lista[@]}"; do
    echo "Item: $item"
done
```

### For Loop (Estilo C)
```bash
for ((i=0; i<10; i++)); do
    echo "Contagem: $i"
done
```

### While Loop
```bash
while [[ "$condicao" == "true" ]]; do
    # código
done
```

## 5. Funções e Retorno
Funções não retornam valores como em Python; elas retornam um **Exit Code** (0-255). Para "retornar" dados, use `echo` e capture com Command Substitution.

```bash
minha_funcao() {
    local arg1="$1"  # Escopo local é essencial
    local arg2="$2"
    
    if [[ -z "$arg1" ]]; then
        return 1 # Erro (Exit Status)
    fi
    
    echo "$((arg1 + arg2))" # "Retorno" de dado
}

# Chamada e Captura
resultado=$(minha_funcao 10 20)
status=$? # Captura o return da última função
```

## 6. Input e Argumentos
Captura de entrada do usuário e argumentos de linha de comando.

```bash
# Argumentos de script: $1, $2, ..., $n
# $@ = todos os argumentos
# $# = número de argumentos

# Input do usuário
read -p "Digite seu nome: " username
read -s -p "Senha: " password # -s para silent (esconde o input)
```

## 7. Aritmética
Bash nativo só suporta inteiros.

```bash
# Sintaxe $(( ))
soma=$((10 + 5))
((contador++))
```

---
### 💡 Dicas de Padrões de Mercado (Enterprise Ready)
* **Shebang:** Sempre use `#!/usr/bin/env bash` para portabilidade.
* **Fail Fast:** Use `set -euo pipefail` no início do script para encerrar em caso de erro ou variáveis não definidas.
* **Shellcheck:** Sempre passe seus scripts no utilitário `shellcheck` para validar boas práticas e segurança.