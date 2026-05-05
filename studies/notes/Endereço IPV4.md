# Endereços e suas propriedades/caracteristicas
## Tabela de tipos de endereço

| Classe | Range de Endereços IP       | Máscara Padrão      | Hosts por Rede | Descrição                                          |
| ------ | --------------------------- | ------------------- | -------------- | -------------------------------------------------- |
| A      | 0.0.0.0 – 127.255.255.255   | 255.0.0.0 (/8)      | 16.777.214     | Redes muito grandes                                |
| B      | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 (/16)   | 65.534         | Redes médias                                       |
| C      | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 (/24) | 254            | Redes pequenas                                     |
| D      | 224.0.0.0 – 239.255.255.255 | —                   | —              | Multicast (não usado para hosts)                   |
| E      | 240.0.0.0 – 255.255.255.255 | —                   | —              | Reservado para uso experimental (novastecnologias) |
## Tipos De envio
**Multicast:** Envia para múltiplos host
**Unicast:** Envia pra um host P to P
**Broadcast** Envio para todos os host da mesma rede ou sub-rede a depender da projeto

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
Para enriquecer seu Obsidian, estruturei os endereços da imagem em uma tabela técnica detalhada. Como você foca em Redes e Segurança, adicionei a fundamentação teórica sobre o porquê de cada bloco existir.

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

## Hosts 
```
Hosts são as maquinas em uma rede, que são indentificadas em uma parte no endereço de rede
```

