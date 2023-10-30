import random
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
                        print("Selecione uma opção válida!1\n")
            else:
                print("Selecione uma opção válida!2\n")


# Abertura do Game

def game():

    # Abertura e sorteio da palavra
    imprime_abertura()
    palavra_secreta = carrega_palavra_secreta()

    #Número de caracteres da forca
    letras_acertadas = ["_" for letras in palavra_secreta]
    print(' '.join(letras_acertadas))

    # Variáveis
    enforcou = False
    acertou = False
    erros = 0


    # Enquanto não esgotar as tentativas e acertar a palavra, repetir a sequencia dentro do while
    while(not enforcou and not acertou ):

        chute = pede_chute()

        # Uso do for baseado em número de tentativas para que sejam recebidos os chutes, possuindo o index como local das letras em sequência
        if (chute in palavra_secreta):
            marca_acerto(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            print("\nOps, você errou! Faltam {} tentativas.\n".format(7 - erros))
            boneco_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(' '.join(letras_acertadas))

    if(acertou):
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
        print("Puxa, você foi enforcado!")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print(" /                   \     ")
        print(" |   XXXX     XXXX   |     ")
        print(" |   XXXX     XXXX   |      ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        print("\nA palavra era {}.".format(palavra_secreta))



def imprime_abertura():
    print("**************")
    print("Jogo da forca!")
    print("**************\n")

# Carrega palavra aleatória
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    sorte = random.randint(0, len(palavras) - 1)
    palavra_secreta = palavras[sorte].upper()
    return palavra_secreta

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_acerto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def boneco_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    play()
