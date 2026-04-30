"""
Simples código que verifica se um número é par ou ímpar
"""

def par(num: int = 0) -> None:
    """_summary_    verifica se o número é par ou ímpar
    Args:
        num (int): número a ser verificado
    """
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")