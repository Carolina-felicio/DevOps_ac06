def pagamento(valor, atraso):

    if valor < 0:
        return None
    elif diasatraso > 0:
        multa = valor * 0.03
        adicionaltraso = valor * (diasatraso * 0.01)
        return valor + multa + adicionalatraso
        return valor
