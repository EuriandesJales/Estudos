
A verdade é que o Ipv4 já foi criado meio obsoleto, devido a sua limitação de número de ips possível, e por esta razão foi criado quase que em conjunto o Ipv6, embora o Ipv4 já tinha cido implementado, desta forma, estamos hoje em um cenário de migração do Ipv4 para o Ipv6, mas afinal:

## Qual é a Diferença de IPV4 pra IPV6?

O número de endereços possíveis seria a primeira e mais significativa diferença.
no ipv4 temos 32 bits com 4.294.967.296 endereços já no ipv6 temos 256 bits totalizando 340 undecilhões(340.282.366.920.938.463.463.374.607.431.768.211.456) de endereços possíveis.

além disso temos coreçoes e ampliações de funcionalidade:
aproveitou para corrigir as limitações do IPv4 e incluir aprimoramentos. Um exemplo é o ICMPv6 (Internet Control Message Protocol versão 6), que inclui a resolução de endereços e a configuração automática de endereços, não encontradas no ICMP para IPv4 (ICMPv4).


![[esgotamento-ipv4.png]]

Hoje coexistimos em um mundo que usa ambas as tecnologias através de técnicas de migração para manter ambos suportes como:
- *pilha dupla* permite que IPv4 e IPv6 coexistam no mesmo segmento de rede. Os dispositivos de pilha dupla executam os protocolos IPv4 e IPv6 simultaneamente.
- *Tunelamento* é um método de transporte de pacote IPv6 através de uma rede IPv4. O pacote IPv6 é encapsulado dentro de um pacote IPv4
- *O NAT64* Camada de tradução de IPV4 pra IPV6

## Diferentes base Númericas

O ipv4 usa base númerica binaria enquanto o sistema IPV6 usa hexadecimal

Elementos Decimais: 

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Elementos Binarios:

| 0   | 1   |
| --- | --- |

Elementos Hexadecimal:

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | A   | B   | C   | D   | E   | F   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Endereçaento IPV6 Hexadecimal

Cada 4 bits são representados por um único dígito hexadecimal, totalizando 32 valores hexadecimais

tendo seus campos indo do range de 0000 até ffff esses 4 digitos Hexadecimais representam 16 digitos binários 

Separador ``:`` Para cada 4 Digitos hexadecimal
IPv6 é x: x: x: x: x: x: x: x
No total temos 8 campos

**IMPORTANTE: O IPV6 NÃO É CASE SENSITIVE (não diferencia maiúsculo de minusculo) **

exemplos de endereços validos:
	
	2001 : 0db8 : 0000 : 1111 : 0000 : 0000 : 0000: 0200
	
	2001 : 0db8 : 0000 : 00a3 : abcd : 0000 : 0000: 1234
	
	2001 : 0db8 : 000a : 0001 : c012 : 9aff : fe9a: 19ac
	
	2001 : 0db8 : aaaa : 0001 : 0000 : 0000 : 0000: 0000
	
	fe80 : 0000 : 0000 : 0000 : 0123 : 4567 : 89ab: cdef
	
	fe80 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0001
	
	fe80 : 0000 : 0000 : 0000 : c012 : 9aff : fe9a: 19ac
	
	fe80 : 0000 : 0000 : 0000 : 0123 : 4567 : 89ab: cdef
	
	0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0001
	
	0000 : 0000 : 0000 : 0000 : 0000 : 0000 : 0000: 0001



```Python


import ipaddress
import sys

def converter_ipv4_completo(ip_str):
    try:
        # Validação técnica via biblioteca padrão
        ip_obj = ipaddress.IPv4Address(ip_str)
        ip_int = int(ip_obj)
        
        # 1. Binário 32-bits
        ip_bin_raw = f"{ip_int:032b}"
        
        # 2. Binário por Octetos
        octetos = ip_str.split('.')
        ip_bin_formatado = ".".join([f"{int(o):08b}" for o in octetos])
        
        # 3. Hexadecimal
        ip_hex = f"0x{ip_int:08X}"
        
        print(f"--- Análise Técnica: {ip_str} ---")
        print(f"Decimal (Int): {ip_int}")
        print(f"Binário (Oct): {ip_bin_formatado}")
        print(f"Hexadecimal:   {ip_hex}")
        print("-" * 34)

    except ValueError:
        print(f"Erro: '{ip_str}' inválido.", file=sys.stderr)
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Teste estático para evitar erro de input no plugin do Obsidian
    ip_teste = "192.168.0.1"
    converter_ipv4_completo(ip_teste)
```

## Processo de encurtamento de IPV4

**Zero a esquerda pode e deve ser obtido.***

![[encurtamento-ipv6.png]]

Grande cadeias de zero no meio do endereço
![[encurtamento ipv6-2.png]]