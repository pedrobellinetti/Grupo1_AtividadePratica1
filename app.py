def mostra_tabuleiros(tabuleiro): 
    print("-" * 20)

    for linha in tabuleiro:
        print(f"|{linha[0]}|{linha[1]}|{linha[2]}")
        print("-" * 20)

def escolher_marcador():
    jogadores = ["X", "O"]
    print(f""" 
    Marcadores disponíveis:
    1: "X"
    2: "O"
    {"-" * 20}
    """)
    escolha = int(input("Escolha o marcador desejado: "))

    if (escolha == 1):
        return jogadores[0]
    else:
        return jogadores[1]


def verifica_vitoria(tabuleiro, jogador):
    # Verifica na horizontal
    for i in range(0, 3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
    
    # Verifica na vertical
    for i in range(0, 3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
        
    # Verifica na diagonal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

