# Cybersecurity Lab (Docker Migration)

Este projeto documenta o estudo e a transição de um laboratório de segurança baseado em Máquinas Virtuais (VMs) para um ambiente totalmente conteinerizado utilizando Docker. O foco é avaliar a viabilidade e a eficiência de ferramentas de pentest em ambientes isolados e leves.  

## 🎯 Objetivos do Projeto

- Migração de Infra: Avaliar o desempenho de ferramentas de segurança em containers comparado ao uso tradicional em VMs.  

- Interface GUI: Testar a funcionalidade e o overhead de aplicações gráficas (GUI) rodando dentro de containers Docker.

- Orquestração de Lab: Criar um ambiente multi-node utilizando Docker Compose, integrando diferentes sistemas operacionais.

- Análise de Interoperabilidade: Testar o potencial das ferramentas do Kali Linux em diferentes dispositivos na mesma rede, observando como as ferramentas interagem com diversos SOs.  

# 🛠️ Fase Atual

- Conteinerização do Kali Linux: Build da imagem base em andamento. 
- X11 Forwarding / VNC: Testando a funcionalidade e o desempenho de aplicações gráficas dentro do container.  

# 🏗️ Estrutura do Laboratório (Roadmap)

O laboratório será composto por três instâncias principais conectadas em uma rede isolada:

- Kali Linux: Container principal de ataque (Attacker Node).  

- Windows Instance: Alvo para testes de exploração e hardening (Victim Node).  

- Web Server: Integração com o projeto Docker Web Lab para testes em aplicações web.  ⚠️ Status do ProjetoEM 

# DESENVOLVIMENTO (WIP)