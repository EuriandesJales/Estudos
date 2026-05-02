# Aplicativo Pomodoro
Escrito em Python.

### O objetivo deste projeto foi entender o processo de empacotamento (packaging) e geração de binários executáveis a partir de código Python.

--- 

##  📦 Baixe e use o app ou compile a partir do código-fonte
🔧 Como compilar o projeto em um executável
🧠 Conceito rápido (base teórica)

Python é uma linguagem interpretada, então não gera binários nativos por padrão.

Ferramentas como PyInstaller fazem o seguinte:

Empacotam o interpretador Python
Incluem dependências (bibliotecas)
Geram um binário standalone (.exe, ELF, etc.)

## 📋 Pré-requisitos
- Python 3 instalado
- Ambiente virtual (recomendado)
- pip atualizado

## Passos
- 🧱 1. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux (Zsh no seu caso)

- 📥 2. Instalar dependências
pip install -r requirements.txt

Se não houver:

pip install pyinstaller

- ⚙️ 3. Gerar executável
Comando básico:
pyinstaller --onefile main.py

### Parâmetros importantes:
| Flag              | Função                     |
| ----------------- | -------------------------- |
| `--onefile`       | Gera um único binário      |
| `--noconsole`     | Remove terminal (apps GUI) |
| `--icon=icon.ico` | Define ícone               |
| `--name`          | Nome do executável         |


- 📂 4. Estrutura gerada
dist/
└── pomodoro-app   # executável final

build/             # arquivos temporários
*.spec             # configuração do build

### 🚀 5. Executar
./dist/pomodoro-app
⚠️ Pontos importantes (níve