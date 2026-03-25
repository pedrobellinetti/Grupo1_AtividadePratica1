# Exibe o tabuleiro
def mostra_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro
    """
    
    print("-------------")
    
    for linha in tabuleiro:
        print(f"|{linha[0]}|{linha[1]}|{linha[2]}|")
        
        print("-------------")

def verifica_vitoria(tabuleiro, jogador):
    """
    Verifica se o jogador (X ou O) venceu o jogo

    Args:
        tabuleiro (list[list[str]]): Matriz 3x3 que representa o tabuleiro
        jogador (str): Símbolo do jogador que será verificado ("X". "O" ou " "(vazio))

    Returns:
        bool: Truye se o jogador venceu, False caso contrário
    """
    
    # Verifica as 3 linhas horizontais
    for i in range(0,3):
        
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            
            return True
    
    # Verifica as 3 colunas verticais
    for i in range(0,3):
        
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            
            return True
    # Verifica a diagonal principal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        
        return True
    
    # Verifica a diagonal secundária
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        
        return True
    
    return False

def verifica_empate(tabuleiro):
    """
    Verifica se o jogo empatou

    Args:
        tabuleiro (list[list[str]]): Matriz 3x3 que é o tabuleiro

    Returns:
        bool: True se todas as casas estão preenchidas, False caso contrário
    """
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def verifica_termino(tabuleiro, jogador, bot):
    if verifica_vitoria(tabuleiro, jogador) or verifica_empate(tabuleiro) or verifica_vitoria(tabuleiro, bot):
        return True
    return False

def minimax(tabuleiro, bot, jogador, vez_do_bot):
    """
    Algoritmo Minimax recursivo

    Args:
        tabuleiro (list[list[str]]): Matriz 3x3 do tabuleiro
        bot (str): Símbolo que o bot está assumindo na partida
        jogador (str): Símbolo que o jogador humano está assumindo na partida
        vez_do_bot (bool): True se for o turno do bot, False se não for

    Returns:
        int: Retorna +1 se o bot vencer. Retorna -1 se o jogador humano vencer. Retorna 0 se houver empate
    """
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

def melhor_jogada(tabuleiro, bot, jogador):
    """
    Encontra e executa a melhor jogada para o bot.

    Args:
        tabuleiro (list[list[str]]): Matriz 3x3, que representa o estado atual do jogo
        bot (str): Símbolo do bot("X" ou "O")
        jogador (str): Símbolo do jogador("X" ou "O") 
    """

    melhor_score = -100 # Pior score possível para o bot
    jogada = (-1, -1) # Coordenada da melhor jogada para o bot (no caso, a pior jogada)

    #Testa cada casa vazia
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                tabuleiro[i][j] = bot

                # Simula jogadas do bot
                score = minimax(tabuleiro, bot, jogador, False)
                tabuleiro[i][j] = " " # Desfaz a simulação
                
                # Se score for melhor que a variável definida ou valor encontrado até o momento
                # Atualiza o melhor_score para score e salva a posição
                if score > melhor_score:
                    melhor_score = score
                    jogada = (i,j)

    # Executa a melhor jogada encontrada
    tabuleiro[jogada[0]][jogada[1]] = bot
    print(f"\nGPeto jogou na linha {jogada[0] + 1}, coluna {jogada[1] + 1}")
    mostra_tabuleiro(tabuleiro)

def start_jogo():
    """
    Função principal que controla o jogo
    """
    
    # Tabuleiro vazio, é uma lista de 3 listas, cada uma com 3 espaços/colunas
    tabuleiro = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    
    # Símbolos possíveis
    simbolos = ["X","O"]
    
    # Loop para escolha de símbolos
    while(True):
        jogador = int(input("""
        Escolha qual simbolo deseja representar:
        1. X
        2. O
        :
        """))
        if jogador == 1:
            jogador = simbolos[0] # Símbolo do jogador = "X"
            bot = simbolos[1] # Símbolo do bot = "O"
            break
        elif jogador == 2:
            jogador = simbolos[1] # Símbolo do jogador = "O"
            bot = simbolos[0] # Símbolo do bot = "X"
            break
        else:
            print("Escolha inválida, tente novamente.") # Retorna até o jogador sair do terminal ou fizer uma escolha válida
    
    mostra_tabuleiro(tabuleiro)
    
    # No máximo 9 jogadas possíveis, pois é uma matriz 3x3
    for i in range(9):
        
        if turno_atual == jogador:
            while True:
                linha = int(input("Escolha uma linha: (1-3): ")) -1 # Pois os índices começam em 0
                coluna = int(input("Escolha uma coluna: (1-3)")) -1

                # Valida se linha e coluna estão dentro do intervalo permitidos
                if 0 <= linha <=2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador
                    break
                # Verifica se a casa está vazia ou não
                else:
                    print("Posição inválida ou ocupada. Tente novamente.")

                    mostra_tabuleiro() # Mostra o estado atual para que a escolha possa ser feita
        else: 
            print("\nVez do bot...")
            melhor_jogada(tabuleiro, bot, jogador)

            # Verificar após o bot jogar

            # Checar se a última jogada já pode ter sido vencedora
            if verifica_vitoria(tabuleiro, jogador):
                print("Jogador venceu!!")
                return
            
            if verifica_vitoria(tabuleiro, bot):
                print("Bot venceu!!")
                return
            
            # Checar se houve empate
            if verifica_empate(tabuleiro):
                print("O jogo terminou empatado")
                return

            # Alternância de turnos

            if turno_atual == "X":
                turno_atual = "O"
            else: 
                turno_atual = "X"

# Inicia o jogo
start_jogo()

