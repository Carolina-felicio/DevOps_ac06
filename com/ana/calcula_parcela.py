"""Arquivo para calculo de parcela
"""

def pagamento(valor, atraso):
    """ Funcao que calcula pagamento
    """
    if valor < 0:
        return valor
    if atraso > 0:
        multa = valor * 0.03
        adicionalatraso = atraso * 0.01
        return multa + adicionalatraso