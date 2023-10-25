import random
def play():
    # Abertura do Game
    print("**************")
    print("Jogo da forca!")
    print("**************\n")

    # Palavra aleatória
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    sorte = random.randint(0, len(palavras)-1)

    # Formata a palavra aleatória e
    palavra_secreta = palavras[sorte].upper()
    letras_acertadas = ["_" for letras in palavra_secreta]

    # Variáveis
    enforcou = False
    acertou = False
    erros = 0

    # Número de letras da palavra aleatória
    print(' '.join(letras_acertadas))

    # Enquanto não esgotar as tentativas e acertar a palavra, repetir a sequencia dentro do while
    while(not enforcou and not acertou ):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        # Uso do for baseado em número de tentativas para que sejam recebidos os chutes, possuindo o index como local das letras em sequência
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(' '.join(letras_acertadas))


        print("Jogando...")

    if(acertou):
        print("Você ganhou!!!")

    else:
        print("Você perdeu!")

if(__name__ == "__main__"):
    play()