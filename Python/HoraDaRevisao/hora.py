def saudacao(hora = 7):
    try:
        if hora < 12:
            return "Bom dia!"
        elif hora < 17:
            return "Boa tarde!"
        elif hora < 24:
            return "Boa noite!"
        else:
            return "Hora inválida!"
    except TypeError:
        return "Erro: o Valor deve ser um número inteiro entre 0 e 24"
    except Exception as e:
        print(f"Erro: {e}")
    ...