Os endereços IPv4 podem ser atribuídos estática ou dinamicamente.

Com uma atribuição estática, o administrador de rede deve configurar manualmente as informações da rede para um host. No mínimo, isso inclui o seguinte:

- **Endereço IP**– Identifica o computador na rede.
- **Máscara de Sub-rede** - Identifica a rede à qual o host está conectado
- **Gateway padrão** – Identifica o dispositivo de rede que o host usa para acessar a Internet ou outra rede remota.
Os endereços estáticos têm algumas vantagens. Por exemplo, são úteis para impressoras, servidores e outros dispositivos de rede que precisam estar acessíveis para clientes na rede

# Dynamic Host Configuration Protocol (DHCP)

- Protocolo de IPV4 que gera ip automaticamente para dispositivos conectados em uma rede.

- O endereço não é permanentemente atribuído a um host, mas é só “alugado” por um período. Se o host é desligado ou retirado da rede, o endereço retorna ao pool para ser reutilizado.

- Vários tipos de dispositivos podem ser servidores DHCP, desde que executem software de serviço DHCP. Na maioria das redes médias a grandes, o servidor DHCP normalmente é um servidor local dedicado baseado em PC.
		 O roteador sem fio é tanto servidor como cliente DHCP. O roteador sem fio atua como cliente para receber a configuração de IPv4 do ISP e atua como servidor DHCP para hosts internos na rede local

## 🏗️ Arquitetura do Handshake (DORA)

### 1. 🔍 **D**iscover (Descoberta)

- **Ação:** O cliente (sua máquina) envia um pacote em **Broadcast** para localizar servidores ativos.
    
- **Camada 2:** MAC de destino `FF:FF:FF:FF:FF:FF`.
    
- **Camada 3:** IP de destino `255.255.255.255`.
    
- **Contexto:** É um "grito" na rede: _"Alguém pode me dar um IP?"_.
    

### 2. 📢 **O**ffer (Oferta)

- **Ação:** O servidor DHCP reserva um IP disponível e responde ao cliente.
    
- **Conteúdo:** Além do IP proposto, envia a máscara de sub-rede, gateway padrão e tempo de **Lease** (concessão).
    
- **Contexto:** O servidor diz: _"Eu tenho o IP 192.168.1.50 disponível por 24 horas, você quer?"_.
    

### 3. 📝 **R**equest (Requisição)

- **Ação:** O cliente aceita formalmente a oferta recebida.
    
- **Importância:** Mesmo sabendo o IP, o cliente ainda envia em broadcast para avisar a outros possíveis servidores DHCP que ele já aceitou uma oferta específica.
    
- **Contexto:** _"Sim, eu aceito esse IP desse servidor específico!"_.
    

### 4. ✅ **A**ck (Confirmação/Acknowledge)

- **Ação:** O servidor confirma a transação e o cliente finaliza sua configuração de rede.
    
- **Resultado:** O cliente passa a utilizar o IP e o servidor marca aquele endereço como "ocupado" em seu banco de dados.
    

---

## 🛠️ Detalhes de Baixo Nível (Para seu Obsidian)

|**Atributo**|**Detalhe Técnico**|
|---|---|
|**Portas UDP**|67 (Servidor) e 68 (Cliente)|
|**Endereço de Destino Inicial**|`255.255.255.255` (Limited Broadcast)|
|**Encapsulamento**|Ethernet -> IP -> UDP -> DHCP|
|**Segurança**|Vulnerável a _DHCP Starvation_ e _Rogue DHCP Servers_ se não houver **DHCP Snooping** no switch.|
**Causa Raiz da Confiabilidade:** O uso do broadcast no `255.255.255.255` garante que, mesmo sem configuração prévia, qualquer dispositivo consiga encontrar o caminho para a internet em uma rede nova.

Ferramentas como o `Wireshark` permitem ver exatamente esses quatro pacotes (Discover, Offer, Request, Ack) acontecendo em tempo real.