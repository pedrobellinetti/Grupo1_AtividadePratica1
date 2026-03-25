#!/usr/bin/env python
# coding: utf-8

# # Parte 1 - Jogo da Velha

# ### Passo 1: Criar uma função que escreve na tela o tabuleiro

# In[ ]:


def mostra_tabuleiro(tabuleiro):
    
    print("-------------") # Marca uma divisão entre telas para controle visual
    
    for linha in tabuleiro:
        
        print("|", linha[0], "|", linha[1], "|", linha[2], "|")
        
        print("-------------") # Marca uma divisão entre telas para controle visual


# ### Passo 2: Criar as regras para que o jogo seja finalizado

# In[ ]:


def verifica_vitoria(tabuleiro, jogador):
    
    # Vamos verificar possibilidade de vitória por sequência horizontal
    for i in range(0,3):
        
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            
            return True
        
    # Vamos verificar possibilidade de vitória por sequência vertical
    for i in range(0,3):
        
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            
            return True
        
    # Vamos verificar possibilidade de vitória na diagonal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        
        return True
    
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        
        return True
    
    return False

def robo(tabuleiro, bot, jogador):
    for linha in range(0, len(tabuleiro)):
        for coluna in range(0, len(tabuleiro)):
            if tabuleiro[0][0] == jogador and tabuleiro[0][2] == jogador and tabuleiro[0][1] == " ":
                tabuleiro[0][1] = bot
                mostra_tabuleiro(tabuleiro)
                return
            if tabuleiro[1][0] == jogador and tabuleiro[1][2] == jogador and tabuleiro[1][1] == " ":
                tabuleiro[1][1] = bot
                mostra_tabuleiro(tabuleiro)
                return
            if tabuleiro[2][0] == jogador and tabuleiro[2][2] == jogador and tabuleiro[2][1] == " ":
                tabuleiro[2][1] = bot
                mostra_tabuleiro(tabuleiro)
                return
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = bot
                mostra_tabuleiro(tabuleiro)
                return

# ### Passo 3: Criar a função que inicializa o jogo

# In[ ]:


def start_jogo():
    
    # Criação da lista que gera o tabuleiro
    tabuleiro = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    
    # Jogadores existentes
    simbolos = ["X","O"]
    
    # Define o marcador que inicia o jogo
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
    
    # Printa o tabuleiro na tela
    mostra_tabuleiro(tabuleiro)
    
    # Definindo o posicionamento dos marcadores
    for i in range(1,10):
        
        linha = int(input("Escolha uma linha 1 - 3: ")) - 1
        coluna = int(input("Escolha uma coluna 1 - 3: ")) - 1
        
        # Verificando se a posicao escolhida e valida
        if tabuleiro[linha][coluna] != " ":
            
            print("Posição ocupada.\nEscolha outra opção.")
            linha = int(input("Escolha uma linha 1 - 3: ")) - 1
            coluna = int(input("Escolha uma coluna 1 - 3: ")) - 1
               
        tabuleiro[linha][coluna] = jogador
        mostra_tabuleiro(tabuleiro)
        
        if verifica_vitoria(tabuleiro, jogador):
            
            print(f"Jogador venceu!!!")
            return

        robo(tabuleiro, bot, jogador)

        if verifica_vitoria(tabuleiro, bot):
            
            print(f"Bot venceu!!!")
            return
        
    # Caso nenhuma das condições de vitória sejam encontradas, devemos considerar o resultado de empate
    print("O jogo terminou empatado.")


# In[ ]:

start_jogo()

