from funcoes import *

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
            linha = int(input("Linha"))
            coluna = int(input("Coluna"))
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

print(frota)