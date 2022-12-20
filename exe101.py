def voto(age):
    """Calcula a situação de possibilidade de voto de um cidadão a partir do seu ano de nascimento

    Args:
        age (int): ano de nascimento do usuario

    Returns:
        str: Retorna a situação de voto
    """

    from datetime import date
    global idade
    idade = date.today().year - age
    if idade >= 18 and idade <= 65:
        return f"Situação com {idade} anos: VOTO OBRIGATORIO"
    if idade >= 16 and idade < 18 or idade > 65:
        return f"Situação com {idade} anos: VOTO OPCIONAL"
    if idade < 16:
        return f"Situação com {idade} anos: IDADE INSUFICIENTE PRA SER ELEITOR"

anonasc = int(input("DIGITE SEU ANO DE NASCIMENTO: "))
print(voto(anonasc))
help(voto)
