"""Arquivo para calculo de parcela
"""

def pagamento(valor, atraso):
    """ Funcao que calcula pagamento
    """
    if valor < 0:
        return None
    if atraso > 0:
        multa = valor * 0.03
        adicionalatraso = valor * atraso * 0.01
        return valor + multa + adicionalatraso