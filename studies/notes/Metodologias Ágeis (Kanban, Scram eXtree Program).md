
# Visão Geral

Metodologias ágeis surgiram como resposta aos modelos tradicionais de gerenciamento de projetos, como o _Waterfall_ (cascata), que eram muito rígidos e lentos para ambientes de mudança constante.

A lógica central do ágil é:

- **entregar valor rapidamente**
    
- **adaptar-se a mudanças**
    
- **trabalhar em ciclos curtos**
    
- **ter feedback constante**
    
- **melhorar continuamente**
    

Agora vamos para as três metodologias na ordem pedida.

---

# 1. Kanban

## O que é?

Kanban é uma metodologia ágil baseada em **visualização do fluxo de trabalho**.

A palavra vem do japonês e significa algo como “cartão visual” ou “sinal”.

O objetivo principal é:

- controlar fluxo
    
- reduzir gargalos
    
- aumentar previsibilidade
    
- evitar sobrecarga da equipe
    

Kanban é extremamente usado em:

- suporte técnico
    
- DevOps
    
- SOC/NOC
    
- desenvolvimento contínuo
    
- equipes de infraestrutura
    
- times de atendimento
    

---

## Como funciona?

A lógica do Kanban é baseada em um **pipeline visual**.

Exemplo clássico:

|To Do|Doing|Done|
|---|---|---|
|tarefas pendentes|em execução|concluídas|

Cada tarefa é um “card”.

Ela vai andando pelo fluxo.

---

## Conceitos importantes

### Fluxo contínuo

Diferente do Scrum, não existem “sprints”.

O trabalho flui continuamente.

---

### WIP Limit (Work In Progress)

Define quantas tarefas podem estar em execução ao mesmo tempo.

Exemplo:

|Coluna|Limite|
|---|---|
|Doing|3 tarefas|

Isso evita:

- multitarefa excessiva
    
- gargalos
    
- burnout
    
- filas invisíveis
    

---

### Gargalo

Se uma coluna acumula muitas tarefas, existe um problema no fluxo.

Exemplo:

```text
To Do: 5
Doing: 2
Review: 15
Done: 1
```

Claramente o processo de revisão virou gargalo.

---

## Como se implementa?

### Passo 1 — Mapear fluxo real

Você identifica como o trabalho acontece.

Exemplo em desenvolvimento:

```text
Backlog → Desenvolvimento → Teste → Deploy → Produção
```

---

### Passo 2 — Criar quadro Kanban

Pode ser:

- físico (post-it)
    
- digital
    

Ferramentas comuns:

- [Trello](https://trello.com/?utm_source=chatgpt.com)
    
- [Jira](https://www.atlassian.com/software/jira?utm_source=chatgpt.com)
    
- [GitHub Projects](https://github.com/features/issues?utm_source=chatgpt.com)
    

---

### Passo 3 — Definir limites de WIP

Exemplo:

|Coluna|Limite|
|---|---|
|Desenvolvimento|3|
|Teste|2|

---

### Passo 4 — Monitorar métricas

Principais métricas:

|Métrica|Significado|
|---|---|
|Lead Time|tempo total da tarefa|
|Cycle Time|tempo em execução|
|Throughput|quantidade entregue|

---

## Lógica arquitetural do Kanban

Kanban trata o sistema como um:

```text
Sistema de filas
```

Muito parecido com:

- redes
    
- processamento distribuído
    
- pipelines Linux
    
- filas de mensagens
    

A ideia é:

```text
Entrada controlada → processamento estável → saída previsível
```

---

---

# 2. Scrum

## O que é?

Scrum é um framework ágil baseado em:

- ciclos curtos
    
- planejamento iterativo
    
- entregas incrementais
    

O Scrum organiza o trabalho em períodos chamados:

```text
Sprint
```

Normalmente:

- 1 semana
    
- 2 semanas
    
- 4 semanas
    

---

## Como funciona?

A lógica central do Scrum é:

```text
Planejar → executar → revisar → melhorar
```

em ciclos repetitivos.

---

## Estrutura do Scrum

### Product Backlog

Lista geral de funcionalidades.

Exemplo:

```text
- login
- cadastro
- API REST
- autenticação JWT
```

---

### Sprint Backlog

Subset do backlog escolhido para a sprint atual.

---

### Sprint

Janela fixa de desenvolvimento.

Durante a sprint:

- foco total
    
- pouca mudança
    
- objetivo definido
    

---

## Papéis do Scrum

|Papel|Função|
|---|---|
|Product Owner|define prioridades|
|Scrum Master|remove impedimentos|
|Dev Team|executa|

---

## Eventos do Scrum

|Evento|Objetivo|
|---|---|
|Sprint Planning|planejar sprint|
|Daily Scrum|alinhamento diário|
|Sprint Review|revisar entrega|
|Retrospective|melhorar processo|

---

## Como se implementa?

### Passo 1 — Criar backlog

Organizar tudo que o produto precisa.

---

### Passo 2 — Definir sprint

Exemplo:

```text
Sprint de 2 semanas
```

---

### Passo 3 — Planejamento

Equipe escolhe tarefas.

---

### Passo 4 — Daily Meeting

Reunião curta diária.

Perguntas clássicas:

```text
- O que fiz?
- O que farei?
- Existe impedimento?
```

---

### Passo 5 — Review e retrospectiva

Review:

- mostra entregas
    

Retrospectiva:

- analisa falhas do processo
    

---

## Lógica arquitetural do Scrum

Scrum trabalha com:

```text
Iterações controladas
```

Muito parecido com:

- ciclos de release
    
- versões incrementais
    
- integração contínua
    

A filosofia é:

```text
Entregar pequeno → validar rápido → corrigir cedo
```

---

## Problema que o Scrum resolve

Antes do ágil:

```text
12 meses de desenvolvimento
↓
produto falha no final
```

Com Scrum:

```text
2 semanas → feedback
2 semanas → feedback
2 semanas → feedback
```

O risco é reduzido continuamente.

---

---

# 3. Extreme Programming (XP)

## O que é?

Extreme Programming é uma metodologia ágil focada principalmente em:

- qualidade de código
    
- práticas de engenharia
    
- feedback rápido
    
- colaboração intensa
    

Enquanto Scrum foca mais em gestão, XP foca fortemente em:

```text
COMO o software é desenvolvido
```

---

## Como funciona?

XP usa práticas técnicas rígidas para reduzir:

- bugs
    
- dívida técnica
    
- falhas arquiteturais
    

A ideia é:

```text
mudanças pequenas + testes constantes + refatoração contínua
```

---

## Principais práticas do XP

|Prática|Objetivo|
|---|---|
|Pair Programming|programação em dupla|
|TDD|testes antes do código|
|Refactoring|melhorar código continuamente|
|CI/CD|integração contínua|
|Small Releases|releases pequenas|
|Collective Ownership|código pertence ao time|

---

## Pair Programming

Dois devs no mesmo código:

|Papel|Função|
|---|---|
|Driver|digita|
|Navigator|revisa lógica|

Objetivo:

- menos bugs
    
- compartilhamento de conhecimento
    
- revisão contínua
    

---

## TDD (Test Driven Development)

Fluxo:

```text
1. criar teste
2. teste falha
3. implementar código
4. teste passa
5. refatorar
```

Lógica:

```text
teste define comportamento esperado
```

---

## Refatoração contínua

Código nunca é considerado “pronto para sempre”.

Sempre pode ser:

- simplificado
    
- desacoplado
    
- otimizado
    

---

## Como se implementa?

### Passo 1 — Automatizar testes

Ferramentas comuns:

- pytest
    
- JUnit
    
- Jest
    

---

### Passo 2 — Implementar CI/CD

Exemplos:

- [GitHub Actions](https://github.com/features/actions?utm_source=chatgpt.com)
    
- [GitLab CI/CD](https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/?utm_source=chatgpt.com)
    
- [Jenkins](https://www.jenkins.io/?utm_source=chatgpt.com)
    

---

### Passo 3 — Adotar TDD

Escrever testes antes da feature.

---

### Passo 4 — Fazer code review contínuo

Via:

- pair programming
    
- pull requests
    
- revisão coletiva
    

---

## Lógica arquitetural do XP

XP trata software como:

```text
um sistema vivo em constante mudança
```

A prioridade é:

```text
facilidade de manutenção
```

Isso é extremamente alinhado com:

- engenharia de software moderna
    
- DevOps
    
- SRE
    
- microserviços
    

---

# Comparação Final

|Aspecto|Kanban|Scrum|XP|
|---|---|---|---|
|Foco|fluxo|gestão iterativa|engenharia|
|Estrutura|contínua|sprints|práticas técnicas|
|Mudanças|a qualquer momento|controladas por sprint|constantes|
|Métrica principal|fluxo|velocidade|qualidade|
|Ideal para|suporte/ops|produto|software complexo|
|Complexidade|baixa|média|alta|

---

# Como empresas combinam isso na prática

Muito comum encontrar:

|Camada|Metodologia|
|---|---|
|Gestão do fluxo|Kanban|
|Planejamento|Scrum|
|Engenharia|XP|

Exemplo real:

```text
Scrum para gestão
+
Kanban para suporte
+
XP para qualidade do código
```

Isso é extremamente comum em times maduros de engenharia.