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

