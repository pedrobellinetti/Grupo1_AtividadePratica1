def mostra_tabuleiro(tabuleiro):
    
    print("-------------")
    
    for linha in tabuleiro:
        
        print("|", linha[0], "|", linha[1], "|", linha[2], "|")
        
        print("-------------")

def verifica_vitoria(tabuleiro, jogador):
    
    for i in range(0,3):
        
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            
            return True
        
    for i in range(0,3):
        
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            
            return True
        
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        
        return True
    
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        
        return True
    
    return False

def verifica_empate(tabuleiro):
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True


def verifica_termino(tabuleiro, jogador, bot):
    if verifica_vitoria(tabuleiro, jogador) or verifica_empate(tabuleiro) or verifica_vitoria(tabuleiro, bot):
        return True
    return False

def minimax(tabuleiro, bot, jogador):
    if verifica_vitoria(tabuleiro, bot):
        return 1
    if verifica_vitoria(tabuleiro, jogador):
        return -1
    if verifica_empate(tabuleiro):
        return 0

    if vez_do_bot:
        melhor = -100

        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == " ":
                    tabuleiro[i][j] = bot
                    score = minimax(tabuleiro, bot, jogador, False)
                    tabuleiro[i][j] = " "
                    melhor = max(melhor, score)
        
        return melhor
            
                else:
                    melhor = 100
                    for i in range(3):
                        for j in range(3):
                            if tabuleiro[i][j] == " ":   
                                tabuleiro[i][j] = jogador
                                score = minimax(tabuleiro, bot, jogador, True)
                                tabuleiro[i][j] = " "
                                melhor = min(melhor, score)

                    return melhor

def start_jogo():
    
    tabuleiro = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    
    simbolos = ["X","O"]
    
    while(True):
        jogador = int(input("Escolha qual simbolo deseja representar:\n[ 1 ] X\n[ 2 ] O\n: "))
        if jogador == 1:
            jogador = simbolos[0]
            bot = simbolos[1]
            break
        elif jogador == 2:
            jogador = simbolos[1]
            bot = simbolos[0]
            break
        else:
            print("Escolha inválida, tente novamente.")
    
    mostra_tabuleiro(tabuleiro)
    
    for i in range(1,10):
        
        linha = int(input("Escolha uma linha 1 - 3: ")) - 1
        coluna = int(input("Escolha uma coluna 1 - 3: ")) - 1
        
        if tabuleiro[linha][coluna] != " ":
            
            print("Posição ocupada.\nEscolha outra opção.")
            linha = int(input("Escolha uma linha 1 - 3: ")) - 1
            coluna = int(input("Escolha uma coluna 1 - 3: ")) - 1
               
        tabuleiro[linha][coluna] = jogador
        mostra_tabuleiro(tabuleiro)
        
        if verifica_vitoria(tabuleiro, jogador):
            
            print(f"Jogador venceu!!!")
            return

        minimax(tabuleiro, bot, jogador)

        if verifica_vitoria(tabuleiro, bot):
            
            print(f"Bot venceu!!!")
            return
        
    print("O jogo terminou empatado.")

start_jogo()

