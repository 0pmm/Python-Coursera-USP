def computador_escolhe_jogada(n,m):
    PcR = 1
    while PcR != m:
        if (n - PcR) % (m+1) == 0:
            return PcR
        else:
            PcR += 1
    
    return PcR

def usuario_escolhe_jogada(n,m):
    jogadavalida = False
    while not jogadavalida:
        UsR = int(input("\nQuantas peças você vai tirar? "))
        if UsR > m or UsR < 1:
            print("\nOops! Jogada inválida! Tente de novo.")
        else:
            jogadavalida = True
    return UsR


def campeonato():
    user = 0
    pc = 0
    npartida = 1
    while npartida <= 3:
        print("**** Rodada",npartida,"****")
        resultado = partida()
        if resultado == "computador":
            pc += 1
        else:
            user += 1
        npartida += 1
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {user} X {pc} Computador")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    VezPC = False
    if n % (m+1) == 0:
        print("\nVocê começa!")
    else:
        print("\nComputador começa!")
        VezPC = True

    while n > 0:
        if VezPC:
            PcR = computador_escolhe_jogada(n,m)
            n = n - PcR
            if PcR == 1:
                print("\nO computador tirou uma peça.")
            else:
                print(f"\nO computador tirou {PcR} peças.")
            VezPC = False
        else:
            UsR = usuario_escolhe_jogada(n,m)
            n = n - UsR
            if UsR == 1:
                print("\nVocê tirou uma peça.")
            else:
                print(f"\nVocê tirou {UsR} peças.")
            VezPC = True

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        elif n != 0:
            print(f"Agora resta apenas {n} peças no tabuleiro.\n")
    
    if VezPC:
        print("Fim do jogo! Você ganhou!")
        return "usuario"
    else:
        print("Fim do jogo! O computador ganhou!")
        return "computador"

print("Bem-vindo ao jogo do NIM!\nEscolha:")
print("1 - Para jogar uma partida isolada")
ModoJogo = int(input("2 - Para jogar um campeonato "))

if ModoJogo == 2:
    print("\nVocê escolheu um campeonato!\n")
    campeonato()
else:
    print()
    partida()
