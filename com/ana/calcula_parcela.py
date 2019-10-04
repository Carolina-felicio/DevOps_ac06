def valorPagamento(valor, diasAtraso):
    """Form a complex number.
    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if (valor < 0):
        return None
    if (diasAtraso > 0):
        multa = valor * 0.03
        adicionalAtraso = valor * (diasAtraso * 0.01)
        return valor + multa + adicionalAtraso
    else:
        return valor