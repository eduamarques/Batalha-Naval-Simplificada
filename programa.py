from funcoes import *
import random



# Definição de frotas

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

sistema_frota = {
    "porta-aviões": {
        "tamanho": 4,
        "quantidade": 1
    },
    "navio-tanque":{
        "tamanho": 3, 
        "quantidade": 2
    },
    "contratorpedeiro": {
        "tamanho": 2,
        "quantidade": 3
    },
    "submarino": {
        "tamanho": 1,
        "quantidade": 4
    }
}

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}



# Definição da própria frota

for nome in sistema_frota:
    navios = 0
    tamanho = sistema_frota[nome]["tamanho"]
    quantidade = sistema_frota[nome]["quantidade"]

    while navios < quantidade:

        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if nome != "submarino":
            orientacao = input("[1] Vertical [2] Horizontal >")
            if orientacao == "1":
                orientacao = "vertical"
            elif orientacao == "2":
                orientacao = "horizontal"
        else:
            orientacao = "vertical"

        while posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
            print("Esta posição não está válida!")
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome != "submarino":
                orientacao = input("[1] Vertical [2] Horizontal >")
                if orientacao == "1":
                    orientacao = "vertical"
                elif orientacao == "2":
                    orientacao = "horizontal"
            else:
                orientacao = "vertical"
        
        preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        navios += 1



# Tabuleiros

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro = posiciona_frota(frota)



# Jogo principal

jogando = True
posicoes_escolhidas = []
posicoes_escolhidas_oponente = []

while jogando == True:

    print(monta_tabuleiros(tabuleiro, tabuleiro_oponente))

    linha = int(input("Jogador, qual linha deseja atacar? "))
    while linha not in range(10):
        print("Linha inválida!")
        linha = int(input("Jogador, qual linha deseja atacar? "))
    
    coluna = int(input("Jogador, qual coluna deseja atacar? "))
    while coluna not in range(10):
        print("Coluna inválida!")
        coluna = int(input("Jogador, qual coluna deseja atacar? "))

    while [linha, coluna] in posicoes_escolhidas:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")

        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha not in range(10):
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))
        
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna not in range(10):
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

    posicoes_escolhidas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    # Vitória ou ataque do oponente

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

        # Ataque do do oponente

    else:
        
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        while [linha, coluna] in posicoes_escolhidas_oponente:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)

        posicoes_escolhidas_oponente.append([linha, coluna])
        print(f"Seu oponente está atacando na linha {linha} e coluna {coluna}")

        tabuleiro = faz_jogada(tabuleiro, linha, coluna)
        if afundados(frota, tabuleiro) == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False