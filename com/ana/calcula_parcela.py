def pagamento(valor, atraso):

    if valor < 0:
        return None
    if diasAtraso > 0:
        multa = valor * 0.03
        adicionalatraso = valor * (diasatraso * 0.01)
        return valor + multa + adicionalatraso
    else:
        return valor
