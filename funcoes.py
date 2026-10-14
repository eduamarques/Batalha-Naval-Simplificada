def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    return posicoes

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    if nome not in frota:
        frota[nome] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    else:
        frota[nome].append(define_posicoes(linha, coluna, orientacao, tamanho))
    return frota