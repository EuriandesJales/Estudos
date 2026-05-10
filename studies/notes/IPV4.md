# Endereços e suas propriedades/características
## Tabela de tipos de endereço

| Classe | Range de Endereços IP       | Máscara Padrão      | Hosts por Rede | Descrição                                          |
| ------ | --------------------------- | ------------------- | -------------- | -------------------------------------------------- |
| A      | 0.0.0.0 – 127.255.255.255   | 255.0.0.0 (/8)      | 16.777.214     | Redes muito grandes                                |
| B      | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 (/16)   | 65.534         | Redes médias                                       |
| C      | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 (/24) | 254            | Redes pequenas                                     |
| D      | 224.0.0.0 – 239.255.255.255 | —                   | —              | Multicast (não usado para hosts)                   |
| E      | 240.0.0.0 – 255.255.255.255 | —                   | —              | Reservado para uso experimental (novastecnologias) |
|        |                             |                     |                |                                                    |
## Tipos De envio
**Multicast:** Envia para múltiplos host
**Unicast:** Envia pra um host P to P
**Broadcast** Envio para todos os host da mesma rede ou sub-rede a depender da projeto

## Grupos de IP

Rede -> Primeiro endereço possível / nome da rede
Host -> Atribuir endereços de computadores
Broadcast -> Ultimo endereço possível dentro da rede
## Endereçamentos IPv4 Especiais e Reservados

|**Bloco CIDR**|**Classificação**|**Finalidade Técnica**|
|---|---|---|
|**10.0.0.0/8**|Privado (RFC 1918)|Utilizado em redes locais (LAN) de grande porte. Oferece mais de 16 milhões de endereços.|
|**172.16.0.0/12**|Privado (RFC 1918)|Bloco para redes internas de médio porte. Abrange de 172.16.0.0 até 172.31.255.255.|
|**192.168.0.0/16**|Privado (RFC 1918)|O padrão para redes domésticas e pequenas empresas. É o mais comum em roteadores SOHO.|
|**127.0.0.0/8**|Loopback|Usado para testes de software e comunicação interna no próprio host (localhost). O tráfego nunca sai da placa de rede.|
|**169.254.0.0/16**|APIPA|_Automatic Private IP Addressing_. Atribuído automaticamente quando o cliente não encontra um servidor DHCP na rede.|
|**0.0.0.0**|Rota Padrão / Inicialização|Em roteamento, representa a "rota default". Em configurações, indica "todas as interfaces" ou um host sem IP ainda definido.|
|**255.255.255.255**|Broadcast Geral|Endereço de difusão limitada. Um pacote enviado para cá atinge todos os hosts do segmento de rede local atual.|

---

### 💡 Conceitos de Nível Profissional

- **RFC 1918 (Address Allocation for Private Internets):** É o documento normativo que define quais IPs não são roteáveis na Internet pública. Isso permite que milhões de redes usem os mesmos IPs internamente sem conflitos globais, utilizando **NAT** (_Network Address Translation_) para sair para a rede externa.
    
- **APIPA (Link-Local):** Se você ver um IP começando com `169.254` no seu Linux, é o sintoma clássico de falha de comunicação com o serviço DHCP ou problemas de cabeamento/autenticação no switch.
    
- **CIDR (Classless Inter-Domain Routing):** A notação `/8`, `/12` ou `/16` indica quantos bits da máscara de sub-rede são fixos para a identificação da rede. Quanto menor o número, maior a quantidade de hosts disponíveis dentro daquele bloco.

## Representação dos octetos
A forma decimal do ipv4 é usado apenas para leitura de humanos ele na verdade é tratado como um conjunto de quatro octetos, ou seja 4 conjuntos de 8 bits ou 4 bytes se assim preferir

Desta vejamos um exemplo de uma mascara de rede

255.255.255.255 = 11111111.11111111.11111111.11111111

```python
import ipaddress

ip = ipaddress.IPv4Address('192.168.1.10')

print(f"IP em Decimal: {ip}")
print(f"IP em Inteiro (32 bits): {int(ip)}")
print(f"IP em Binário: {bin(int(ip))}")

```
## Hosts 

*Host são as maquinas em uma rede, que são identificadas em uma parte no endereço de rede*

| Classe | Range de Endereços IP       | Máscara Padrão      | Hosts por Rede | Descrição                        |
| ------ | --------------------------- | ------------------- | -------------- | -------------------------------- |
| A      | 0.0.0.0 – 127.255.255.255   | 255.0.0.0 (/8)      | 16.777.214     | Redes muito grandes              |
| B      | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 (/16)   | 65.534         | Redes médias                     |
| C      | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 (/24) | 254            | Redes pequenas                   |
| D      | 224.0.0.0 – 239.255.255.255 | —                   | —              | Multicast (não usado para hosts) |
| E      | 240.0.0.0 – 255.255.255.255 | —                   | —              | Reservado para uso experimental  |

### Caso Não tenha ficado claro
- *A ->* A Rede é por o primeiro octeto resto representa o host 
		```Rede . Host . Host . Host```
- *B ->* A Rede é representada por o primeiro e segundo octeto resto Host
		```Rede . Rede . Host . Host```
- *C ->* 3 octetos = Rede ultimo octeto Host
		```Rede . Rede . Rede . Host```

# Mascaras de Rede

É o conjunto de octetos que permite esconder a rede mostrando o endereço do Host
## Fluxo convencional de máscara baseado no tipo de rede
A masca de Rede padrão é 
```255.255.255.255 = 11111111.11111111.11111111.11111111```
Nesta mascara temos uma dedução que tudo é rede, e a rede se torna oculta através do 255
seguindo esta lógica só precisamos aplicar 255 em cada octeto que representa a rede .
*Exemplos*
- Classe A -> 10.0.12.15 Máscara -> 255.0.0.0 Rede representada por 1 octeto
		``` 11111111.00000000.00000000.00000000```
- Classe B -> 172.16.0.10 Máscara -> 255.255.0.0. Rede representada por 2 octetos
		``` 11111111.11111111.00000000.00000000```
- Classe C -> 192.168.0.1 Máscara -> 255.255.255.0. Rede representada por 3  octetos
		``` 11111111.11111111.11111111.00000000```

***OBS:*** o padrão de número de rede na verdade não é o que define a rede e sim a máscara, embora seja fortemente recomendado sempre seguir os ranges padronizados.

## Conversão de binários 

<iframe width="560" height="315"
src="https://www.youtube.com/embed/Qs0xC9gDU94?start=310&end=387"
title="YouTube video player"
frameborder="0"
allowfullscreen>
</iframe>



## Máscaras CIDR
Historicamente, o IPv4 era dividido em classes fixas (A, B e C). O CIDR aboliu essa rigidez, introduzindo a **notação de barra (prefixo)** para indicar quantos bits do endereço de 32 bits pertencem à rede.

### 1. A Lógica dos Bits

A máscara define quais bits estão "ligados" (valor 1) para identificar a rede:

- Cada octeto possui **8 bits**.
    
- O valor decimal **255** representa um octeto onde todos os 8 bits são `1` ($128+64+32+16+8+4+2+1 = 255$).
    
- A notação `/X` é simplesmente a contagem total de bits `1` da esquerda para a direita.
    

### 2. Equivalência de Classes (Padrão Legado)

|**Notação CIDR**|**Máscara Decimal**|**Antiga Classe**|**Explicação Técnica**|
|---|---|---|---|
|**/8**|255.0.0.0|Classe A|Os primeiros 8 bits são rede. Sobram 24 bits para hosts (~16 milhões).|
|**/16**|255.255.0.0|Classe B|Os primeiros 16 bits (2 octetos) são rede. Sobram 16 bits para hosts (65.534).|
|**/24**|255.255.255.0|Classe C|Os primeiros 24 bits (3 octetos) são rede. Sobram 8 bits para hosts (254).|
#### Máscaras CIDR aplicada a Redes que não são 255
![[máscara-CIDR.png]]

### Sub-Redes Validas
**Uma Máscara de Sub-Rede só é Válida quando não tem 0 entre seus bits 1
- 255
- 254
- 252
- 248
- 240
- 224
- 192
- 128
- 0

### logica na divisão de faixas de endereço ip
![[faixas de endereços de rede logica.png]]


- *REDE ->*  Primeiro IP possível
- *Host ->* Faixa de endereço que esta entre o primeiro IP positivável(Rede) + 1 até o Ultimo endereço possível (Broadcast) - 1
- *BROADCAST ->* O ultimo IP disponível na rede
#### Padrão do Mercado
|**Faixa/Endereço**|**Função Técnica**|**Descrição e Boas Práticas**|
|---|---|---|
|**.0**|**Rede**|Identificador lógico. Nunca atribuído a hosts.|
|**.1** (ou **.254**)|**Gateway Padrão**|A interface do roteador. No Brasil, o `.1` é o mais comum; em redes legadas ou específicas, usa-se o `.254` (o penúltimo).|
|**.2** a **.10**|**Infraestrutura Crítica**|IPs estáticos para Switches core, Controladoras AP e Firewalls secundários.|
|**.11** a **.50**|**Servidores/Serviços**|IPs estáticos para servidores Linux (Docker hosts, bancos de dados, etc.).|
|**.51** a **.200**|**Pool DHCP (Clientes)**|Faixa dinâmica para dispositivos de usuários (Laptops, Mobile).|
|**.201** a **.250**|**Periféricos**|Impressoras, Câmeras (CFTV) e dispositivos IoT.|
|**.251** a **.254**|**Gerência/Reserva**|IPs reservados para acesso administrativo ou gateways de redundância.|
|**.255**|**Broadcast**|Endereço de difusão para toda a sub-rede.|

## 🏗️ A Lógica do Empréstimo de Bits

Imagine que a Máscara de Rede é uma fronteira. Para criar sub-redes, nós movemos essa fronteira para a **direita**, avançando sobre o território que antes pertencia aos hosts.

### O Processo Passo a Passo:

1. **Escolha o Alvo:** Você começa com uma rede padrão, por exemplo, uma **Classe C (`/24`)**.
    
    - Binário: `11111111.11111111.11111111`.`00000000`
        
2. **O Empréstimo:** Se você precisa de **duas** sub-redes, você precisa de 1 bit extra para a rede ($2^1 = 2$).
    
    - A nova máscara se torna **`/25`**.
        
    - Binário: `11111111.11111111.11111111`.`10000000`
        
3. **O Resultado Decimal:** O bit emprestado tem valor **128**. Logo, sua nova máscara é `255.255.255.128`.
    

---

### 📊 Tabela de Divisão (Variação do 4º Octeto)

Quando você "quebra" uma rede `/24`, o último octeto da máscara deixa de ser `.0`. Veja os padrões mais comuns de mercado:

| **Bits Emprestados** | **Nova Máscara (CIDR)** | **Máscara Decimal** | **Sub-redes Criadas** | **Hosts por Sub-rede** |
| -------------------- | ----------------------- | ------------------- | --------------------- | ---------------------- |
| **1 bit**            | `/25`                   | `255.255.255.128`   | 2                     | 126                    |
| **2 bits**           | `/26`                   | `255.255.255.192`   | 4                     | 62                     |
| **3 bits**           | `/27`                   | `255.255.255.224`   | 8                     | 30                     |
| **4 bits**           | `/28`                   | `255.255.255.240`   | 16                    | 14                     |

---

### 🧬 Como identificar as faixas (O Pulo do Gato)

Para saber onde cada sub-rede começa e termina, você usa o **Número Mágico** (ou Incremento).

> **Fórmula:** $256 - \text{Valor do Octeto da Máscara}$

**Exemplo com `/26` (Máscara `.192`):**

- Cálculo: $256 - 192 = 64$.
    
- As redes vão pular de 64 em 64:
    
    1. **Rede 1:** `192.168.1.0` a `.63`
        
    2. **Rede 2:** `192.168.1.64` a `.127`
        
    3. **Rede 3:** `192.168.1.128` a `.191`
        
    4. **Rede 4:** `192.168.1.192` a `.255` 
## VLSM Máscara de tamanho variável


*Sub-Redes variável 
	Vamos a um exemplo pratico:*

Uma Rede *192.168.0.0/24* precisa ser divididas em 4 Sub Redes de tamanhos diferentes
- Lab -> 20
- Secretaria -> 60
- Call-center -> 120
- Coordenação -> 6

120, 60, 20 e 6 Agora ache a mascara de rede da maior
255.255.255.128 Agora converta pra binário

***Máscara do Call-center 255.255.255.128***
  Passo 1 Organizar do maior pra o menor 
	  
	
| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
128
	11111111. 11111111.11111111.10000000 = 255.255.255.128 quantos computadores cabem? Número de host é = a Números  0 na máscara elevado a 2
		Que aqui é 7^2 = 128-2 = 126

***Máscara da Secretaria 60 Hosts = 255.255.255.192***

| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   |
128+64 = 192 
Tamanho da Rede 64 - 2 = 60
***Pois pra ser uma rede não pode ter alternância de bits 0 e 1

255.255.255.192 Máscara de Rede para 60 Dispositivos

***Máscara do Lab 20 hosts ->  255.255.255.224

| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   |
128+64+32 = 224
255.255.255.224 32 Hosts - 2 = *30 Hosts*

***Mascara coordenação 6 -> 255.255.255.248

| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 1   | 1   | 1   | 1   | 0   | 0   | 0   |
128+64+32+16+8 = 248 
Mascara 255.255.255.248 N host = 3^2 = *6 Hosts* 
### Estrutura da Rede
| **Departamento** | **Máscara Decimal** | **Prefixo (CIDR)** | **Cálculo do Salto** | **Tamanho do Bloco (Salto)** | **Hosts Úteis** |
| ---------------- | ------------------- | ------------------ | -------------------- | ---------------------------- | --------------- |
| **LAB**          | `255.255.255.128`   | `/25`              | $256 - 128$          | **128**                      | 126             |
| **SEC**          | `255.255.255.192`   | `/26`              | $256 - 192$          | **64**                       | 62              |
| **CALL**         | `255.255.255.224`   | `/27`              | $256 - 224$          | **32**                       | 30              |
| **COORD**        | `255.255.255.248`   | `/29`              | $256 - 248$          | **8**                        | 6               |
|                  |                     |                    |                      |                              |                 |

| **Endereço de REDE** | **Faixa de HOSTS (Unicast)** | **Endereço de BROADCAST** | **Tamanho do Salto** |
| -------------------- | ---------------------------- | ------------------------- | -------------------- |
| `192.168.0.0`        | `192.168.0.1` até `.126`     | `192.168.0.127`           | 128 IPs (`/25`)      |
| `192.168.0.128`      | `192.168.0.129` até `.190`   | `192.168.0.191`           | 64 IPs (`/26`)       |
| `192.168.0.192`      | `192.168.0.193` até `.222`   | `192.168.0.223`           | 32 IPs (`/27`)       |
| `192.168.0.224`      | `192.168.0.225` até `.230`   | `192.168.0.231`           | 8 IPs (`/29`)        |
| `192.168.0.232`      | `192.168.0.233`até           | **DEPENDE**               | _Próximo salto_      |
|                      |                              |                           |                      |
