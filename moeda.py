def metade(preco=0, formatado = False):
    """calculo da metade

    Args:
        preco (int, optional): recebe o valor informado pelo usuario. Defaults to 0.
        formatado (bool, optional): define se o valor sera retornado formatado ou não. Defaults to False.

    Returns:
        _type_: retorna o valor de acordo com o definido.
    """
    res = preco/2
    return res if formatado is False else formato(res)
    
def dobro(preco=0, formatado = False):
    res = preco*2
    return res if formatado is False else formato(res)

def aumento(preco=0, taxa=0, formatado = False):
    res = preco + (preco*taxa)/100
    return res if formatado is False else formato(res)

def diminuir(preco=0, taxa=0, formatado = False):
    res = preco - (preco*taxa)/100
    return res if formatado is False else formato(res)

def formato (preco = 0, moeda="R$"):
    """FORMATAÇÃO DE UM PREÇO PARA REAL R$

    Args:
        preco (int, optional): Recebe o preço informado. Defaults to 0.
        moeda (str, optional): define a moeda inicialmente como real. Defaults to "R$".

    Returns:
        str: Retorna o valor formatado
    """
    return f"R$ {moeda}{preco:.2f}".replace(".", ",")


def resumo (preco = 0, aum = 0, red = 0):
    """Retorna os valores de forma mais simples no chamado

    Args:
        preco (int, optional): recebe o valor informado. Defaults to 0.
        aum (int, optional): recebe o aumento informado para o calculo da função "aumento". Defaults to 0.
        red (int, optional): recebe o valor de desconto para o calculo da função "diminuir". Defaults to 0.
        formato (bool, optional): retorna o valor formatado ou não. Defaults to False.
    """
    print("="*30)
    print("calculos".center(30))
    print("="*30)
    print(f"1 - Dobro: \t{dobro(preco, True)}")
    print(f"2 - Metade: \t{metade(preco, True)}")
    print(f"3 - {aum}% Aumento: {aumento(preco, aum, True)}")
    print(f"4 - {red}% Redução: {diminuir(preco, red, True)}")