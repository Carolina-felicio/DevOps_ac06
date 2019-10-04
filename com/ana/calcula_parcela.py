def pagamento(valor, atraso):

 """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """

    if valor < 0:
        return None
    elif diasatraso > 0:
        multa = valor * 0.03
        adicionaltraso = valor * (diasatraso * 0.01)
        return valor + multa + adicionalatraso
        return valor
