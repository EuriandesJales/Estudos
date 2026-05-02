def nome(nome=""):
    """
    Função que retorna o tamanho do nome.
    """
    try:
        if len(nome) <= 4:
            return "Nome muito curto!"
        elif len(nome) <= 6:
            return "Nome aceitável!"
        elif len(nome) > 6:
            return "Nome muito longo!"
        ...
    except Exception as e:
       print(f"Erro: {e}")

