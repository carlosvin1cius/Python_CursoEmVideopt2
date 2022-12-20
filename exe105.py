sit = {'total': 0, 'Maior nota': 0, 'Menor Nota': 0, 'Média': 0}
def notas(*n, situ = False):
    """Função analisa as notas de um ou varios alunos

    Args:
        n (int): Uma ou varias notas para analise.
        situ (bool, optional): Indica se sera imprimida ou não a situação dos alunos. Defaults to False.

    Returns:
        dict: Retorna um dictionary com todas as possibilidades: (Total de notas, maior nota, menor nota, média, situação)
    """
    somanotas = 0
    for i in n:
        somanotas += i
        if sit['total'] == 0:
            sit['Maior nota'] = i
            sit['Menor Nota'] = i
        else:
            if i > sit['Maior nota']:
                sit['Maior nota'] = i
            if i < sit['Menor Nota']:
                sit['Menor Nota'] = i
        sit['total'] += 1
    sit['Média'] = somanotas/sit['total']
    if situ == True:
        if sit['Média'] > 7:
            sit['Situação'] = "Aprovado"
        elif 5 <= sit['Média'] < 7:
            sit['Situação'] = "Recuperação"
        else:
            sit['Situação'] = "Reprovado"
    return sit

resp = notas(8, 7, 10, 6, situ=True)
print(resp)