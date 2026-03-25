def mostra_tabuleiros(tabuleiro): 
    print("-" * 20)

    for linha in tabuleiro:
        print(f"|{linha[0]}|{linha[1]}|{linha[2]}")
        print("-" * 20)

