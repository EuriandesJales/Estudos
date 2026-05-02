
# 🛠️ Manual Rápido do **UV** — Gerenciador de Pacotes Python Rápido

> Ferramenta moderna para criar e gerenciar ambientes virtuais Python e dependências de forma rápida e segura.

---

## 🚀 1. Inicializar um projeto com **UV**

```bash
uv init meu_projeto
```

- 🔹 Cria uma nova pasta chamada `meu_projeto`.
- 🔹 Inicializa o projeto UV dentro dela.
- 🔹 Cria arquivos de configuração necessários (ex: `pyproject.toml` ou equivalentes UV).
- 🔹 Prepara o ambiente para gerenciar dependências.

---

## 📦 2. Adicionar uma dependência

```bash
uv add requests
```

- 🔸 Adiciona a biblioteca `requests` como dependência do projeto.
- 🔸 Se o ambiente virtual ainda não existir, cria automaticamente.
- 🔸 Instala `requests` dentro do ambiente virtual isolado.
- 🔸 Atualiza os arquivos de controle do projeto para garantir reprodutibilidade.

---

## 🐚 3. Abrir um shell com o ambiente virtual ativo

```bash
uv shell
```

- 🔹 Abre um terminal com o ambiente virtual do projeto ativado.
- 🔹 Você pode executar comandos como `python` e `pip` dentro desse ambiente isolado.
- 🔹 Ideal para rodar scripts ou instalar bibliotecas manualmente.

---

## ➕ 4. Instalar uma biblioteca manualmente dentro do ambiente virtual UV

```bash
uv shell
pip install nome-da-biblioteca
exit
```

- 🔸 Usa `uv shell` para entrar no ambiente virtual.
- 🔸 Executa o comando `pip install` para instalar uma biblioteca manualmente.
- 🔸 Sai do ambiente com `exit`.
- ⚠️ **Recomendação:** Prefira usar `uv add` para manter o controle de dependências e evitar inconsistências.

---
## 4. Instalação de biblioteca 2° Forma

### Opção 1: Usar o próprio comando do UV para adicionar dependências (recomendado)

O jeito mais seguro, prático e recomendado é usar o próprio comando:
```
uv add nome-da-biblioteca
```
**Por quê?**

- UV vai cuidar de criar o venv (se ainda não existir),
    
- instalar a biblioteca dentro do venv,
    
- atualizar os arquivos de controle (lockfiles),
    
- e garantir que o ambiente esteja consistente.
## 📋 5. Recapitulando os comandos principais

| Comando                 | O que faz                                           |
|-------------------------|----------------------------------------------------|
| `uv init <projeto>`     | Cria e inicializa um projeto gerenciado pelo UV.   |
| `uv add <pacote>`       | Adiciona e instala uma dependência no projeto.     |
| `uv shell`              | Abre um shell com o ambiente virtual ativado.      |
| `pip install ...` dentro do `uv shell` | Instala pacotes manualmente no venv do UV.  |

---

## ✔️ 6. Boas práticas

- 🔹 Prefira sempre usar `uv add` para adicionar dependências.
- 🔹 Evite usar `pip install` fora do `uv shell` para não instalar fora do ambiente.
- 🔹 Use o arquivo de lock gerado para garantir que o ambiente seja reproduzível.
- 🔹 Mantenha seu ambiente virtual isolado para segurança e controle

---

## 🔗 7. Links úteis

- [🌐 UV - Projeto oficial](https://astral.sh/uv/)
- [📚 Documentação UV](https://astral.sh/uv/docs/)
- [📄 PEP 517 & PEP 518 - Especificações de build em Python](https://peps.python.org/pep-0517/)

---

*Manual criado por* **Euriandes — Estudante de Cybersecurity**
