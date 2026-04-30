# simplificador.py
# Um simplificador matemático interativo no terminal, com múltiplas técnicas

import math
import sys
from fractions import Fraction


def menu():
    print("\n=== Simplificador CLI ===")
    print("1. Calcular fatorial simplificado")
    print("2. Simplificar fração")
    print("3. Multiplicação inteligente")
    print("4. Decomposição distributiva")
    print("5. Decomposição em potências de 10")
    print("6. Fator comum em evidência")
    print("7. Aproximação racional")
    print("8. Fatoração básica")
    print("9. Sair")
    return input("Escolha uma opção: ")


def simplificar_fatorial():
    print("\n>>> Calcular fatorial simplificado")
    num = int(input("Digite o número fatorial (ex: 10 para 10!): "))
    base = int(input("Deseja simplificar com base em qual fatorial? (ex: 7 para 7!): "))
    if base > num:
        print("Base maior que o número fatorial!")
        return
    resultado = 1
    for i in range(num, base, -1):
        resultado *= i
    print(f"Resultado simplificado: {resultado}")


def simplificar_fracao():
    print("\n>>> Simplificar fração")
    num = int(input("Numerador: "))
    den = int(input("Denominador: "))
    fator = math.gcd(num, den)
    print(f"Fração simplificada: {num // fator}/{den // fator}")


def multiplicacao_inteligente():
    print("\n>>> Multiplicação com padrão especial")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    if a % 10 == 5 and a == b:
        n = a // 10
        print(f"Reconhecido padrão especial: ({n} × {n+1})|25")
        print(f"Resultado: {n * (n + 1)}25")
        return
    print(f"Resultado: {a * b}")


def decompor_multiplicacao():
    print("\n>>> Decomposição distributiva")
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    a1 = a // 10 * 10
    a2 = a % 10
    b1 = b // 10 * 10
    b2 = b % 10
    print(f"({a1} + {a2}) × ({b1} + {b2})")
    resultado = a1 * b1 + a1 * b2 + a2 * b1 + a2 * b2
    print(f"Resultado: {resultado}")


def decomposicao_potencias():
    print("\n>>> Decomposição em potências de 10")
    n = int(input("Digite o número: "))
    m = int(input("Multiplicador: "))
    partes = [int(d + '0' * (len(str(n)) - i - 1)) for i, d in enumerate(str(n)) if d != '0']
    print("Decomposição:", ' + '.join(map(str, partes)))
    resultado = sum(p * m for p in partes)
    print(f"Resultado: {resultado}")


def fator_comum():
    print("\n>>> Evidenciar fator comum")
    a = int(input("Termo 1: "))
    b = int(input("Termo 2: "))
    f = math.gcd(a, b)
    print(f"Fator comum: {f} → {a} + {b} = {f}({a//f} + {b//f})")
    print(f"Resultado: {a + b}")


def aproximacao_racional():
    print("\n>>> Aproximação racional")
    a = int(input("Número base (ex: 98): "))
    b = int(input("Multiplicador (ex: 5): "))
    base = (a // 10 + 1) * 10
    delta = base - a
    print(f"Usando {base} × {b} - {delta} × {b} = {base*b - delta*b}")
    print(f"Resultado: {a*b}")


def fatoracao_basica():
    print("\n>>> Fatoração básica")
    n = int(input("Digite o número a fatorar: "))
    fatores = []
    d = 2
    while n > 1:
        while n % d == 0:
            fatores.append(d)
            n //= d
        d += 1
    print("Fatores primos:", ' × '.join(map(str, fatores)))

# Codigo principal
if __name__ == "__main__":
    while True:
        escolha = menu()
        if escolha == "1":
            simplificar_fatorial()
        elif escolha == "2":
            simplificar_fracao()
        elif escolha == "3":
            multiplicacao_inteligente()
        elif escolha == "4":
            decompor_multiplicacao()
        elif escolha == "5":
            decomposicao_potencias()
        elif escolha == "6":
            fator_comum()
        elif escolha == "7":
            aproximacao_racional()
        elif escolha == "8":
            fatoracao_basica()
        elif escolha == "9":
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida.")
            