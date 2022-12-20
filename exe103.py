def ficha(nome="", gols=0):
    """GERA A FICHA DE UM JOGADOR

    Args:
        nome (str, optional): Recebe o nome do jogador. Defaults to "".
        gols (int, optional): Receb quantos gols foram marcados. Defaults to 0.
    """
    if nome == "":
        nome = "<desconhecido>"
    if gols == 0:
        gols = 0
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

name = str(input("NOME DO JOGADOR: "))
ngols = str(input("NUMERO DE GOLS: "))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if name.strip == "":
    ficha(gols=ngols)
else:
    ficha(name, ngols)