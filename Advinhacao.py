# Importar bibliotecas
import random
import time
import Jogos

def play():
    game_mode = 0
    while (game_mode == 0):
        game()
        jogar_novamente = input("\n Deseja jogar novamente?(Sim/Não)")
        jogar_novamente = jogar_novamente.upper()
        game_func = 0
        while (game_func == 0):
            if (jogar_novamente == "SIM"):
                print()
                game_mode = 0
                game_func = 1
            elif (jogar_novamente == "NÃO"):
                ir_menu = input("\n Deseja retornar ao menu principal?(Sim/Não)")
                ir_menu = ir_menu.upper()
                while True:
                    if (ir_menu == "SIM"):
                        print()
                        Jogos.menu()
                    elif (ir_menu == "NÃO"):
                        game_func = 1
                        game_mode = 1
                        break
                    else:
                        print("Selecione uma opção válida!\n")
            else:
                print("Selecione uma opção válida!\n")

def game():
    # Abertura do Game
    imprime_abertura()

    # Escolhendo a dificuldade do Game
    dificuldade = seleciona_dificuldade()

    # Sorteando o número e definindo o número de tentativas(sempre será uma a menos que o número digitado se "for" for usado)
    sorte = random.randint(1, dificuldade)
    tentativas = 6
    print("\nSorteando o número!\n")
    time.sleep(2)

    # Uso do "for" para o looping sequenciado de acordo com o número de tentativas
    correto = looping_valor(dificuldade, tentativas, sorte)

    # Finalização
    final(correto, sorte)

def imprime_abertura():
    print("*****************")
    print("Advinhe o número!")
    print("***************** \n")

def seleciona_dificuldade():
    while True:
        dif = input("Selecione digitando a primeira letra da dificuldade: \n     Fácil(1-10) \n     Média(1-100) \n     Difícil(1-1000) \n\n     Selecione: ")
        if dif.lower() == "f":
            return 10
        elif dif.lower() == "m":
            return 100
        elif dif.lower() == "d":
            return 1000
        else:
            print("Valor inválido!\n")

def looping_valor(dificuldade, tentativas, sorte):
    for rodada in range(1, tentativas):
        print("Tentativa {} de {}".format(rodada, tentativas - 1))
        chute = int(input("Digite o seu número: "))

        # Intervalos permitidos
        if (dificuldade == 10):
            if (chute < 1 or chute > 10):
                intervalo = "1 e 10"
                print(f"\nVocê deve digitar um número entre {intervalo}.\n")
                continue
        elif (dificuldade == 100):
            if (chute < 1 or chute > 100):
                intervalo = "1 e 100"
                print(f"\nVocê deve digitar um número entre {intervalo}.\n")
                continue
        elif (dificuldade == 1000):
            if (chute < 1 or chute > 1000):
                intervalo = "1 e 1000"
                print(f"\nVocê deve digitar um número entre {intervalo}.\n")
                continue
        correto = chute == sorte
        maior = chute > sorte
        menor = chute < sorte

        if (correto):
            print("Parabéns, você acertou! \n")
            break
        elif (maior):
            print("Você errou! O seu chute foi maior que o número secreto \n")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto \n")
    return correto

def final(correto, sorte):
    if (correto):
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.      |) |    ")
        print("      '-|:.      |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
        print(" Parabéns, você ganhou!")
    else:
        print(f"Fim de jogo!")
        print("        _)/_")
        print("       (_' <")
        print("         )(_")
        print("   ,--.'''-`'.")
        print("  :.'  :  =- :")
        print("  |:   | ._|]|")
        print("  |____|_____|")
        print(" /.:. /-_-_/")
        print("(.:: / |=|")
        print(" `--'  |=|")
        print("       |=|")
        print(f"infelizmente não foi dessa vez, o número era: {sorte}.")

if(__name__ == "__main__"):
    play()