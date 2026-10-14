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

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro

def posiciona_frota(frota):
    grid = [ [0]*10 for _ in range(10)] # Criação de matriz 10 X 10 ensinada pelo professor --> Não houve verificação em Praire Learn
    for navios in frota.values():
        for navio in navios:
            for posicao in navio:
                grid[posicao[0]][posicao[1]] = 1
    return grid