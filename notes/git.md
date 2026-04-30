# 🛠️ Git Cheat Sheet: Enterprise Edition

## 1. Configuração de Identidade

Antes de qualquer operação, defina quem é você no histórico do projeto.

Bash

```
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

---

## 2. Ciclo de Vida do Arquivo

O fluxo básico de trabalho para o dia a dia.

|**Comando**|**Descrição**|
|---|---|
|`git status`|Verifica o estado atual (UnTracked, Modified, Staged).|
|`git add .`|Move todas as alterações para a **Staging Area**.|
|`git commit -m "msg"`|Cria um snapshot das alterações na **Local Database**.|
|`git push`|Sincroniza o repositório local com o **Remote**.|
|`git log --oneline`|Exibe o histórico de forma simplificada.|

---

## 3. Gestão de Ramificações (Branches)

Essencial para manter o código de produção seguro enquanto você testa novos scripts.

- **Listar:** `git branch`
    
- **Criar:** `git branch <nome-da-branch>`
    
- **Trocar:** `git checkout <nome>`
    
- **Criar e Trocar (-b):** `git checkout -b <nome>`
    
- **Mesclar (Merge):** `git merge <branch-origem>` (Une a origem à branch atual).
    
- **Deletar:** `git branch -d <branch>`
    

---

## 4. Sincronização Remota

Como conectar seu Arch Linux ao GitHub/GitLab.

Bash

```
git remote -v               # Lista URLs remotas (verificar se é SSH ou HTTPS)
git remote add origin <url> # Vincula o repositório local a um servidor
git pull origin <branch>    # Traz as novidades do servidor e mescla
git fetch                   # Baixa as novidades sem aplicar ao seu código
```

---

## 5. Recuperação e Hardening (Desfazer Alterações)

Indispensável quando um script de automação não sai como o esperado.

> [!WARNING]
> 
> Cuidado com comandos de `reset`, eles podem apagar trabalho não comitado.

- **`git restore <file>`**: Descarta mudanças no arquivo que ainda não foram para o `add`.
    
- **`git reset HEAD <file>`**: Retira o arquivo da zona de preparação (Staging).
    
- **`git revert <commit>`**: Cria um novo commit que desfaz exatamente o que um commit antigo fez (forma mais segura em projetos colaborativos).
    
- **`git stash`**: "Esconde" as mudanças atuais para limpar o diretório sem perder o código. Use `git stash pop` para recuperar.
    

---

## 6. Padronização de Mercado (Conventional Commits)

Siga este padrão para que seus repositórios de estudo pareçam profissionais.

**Estrutura:** `tipo(escopo): descrição curta`

- `feat`: Nova funcionalidade (ex: um novo script de segurança).
    
- `fix`: Correção de bug.
    
- `docs`: Alteração apenas em documentação (como este arquivo).
    
- `refactor`: Mudança no código que não altera comportamento (melhorar legibilidade).
    

---

## 💡 Dicas de Fluxo (Workflow)
    
- **Git Diff:** Sempre use `git diff` antes de dar um `git add .` para ter certeza do que está enviando.