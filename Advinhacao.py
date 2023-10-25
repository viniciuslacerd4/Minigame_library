# Importar bibliotecas
import random
import time

def play():
    # Abertura do Game
    print("*****************")
    print("Advinhe o número!")
    print("***************** \n")

    # Escolhendo a dificuldade do Game
    dif_aceita = 0
    while dif_aceita < 1:
        dif = input("Selecione digitando a primeira letra da dificuldade: \n     Fácil(1-10) \n     Média(1-100) \n     Difícil(1-1000) \n\n     Selecione: ")
        if(dif == "f" or dif == "F"):
            dificuldade = 10
            dif_nome = "Fácil"
            dif_aceita += 1
            intervalo = "1 e 10"
        elif (dif == "m" or dif == "M"):
            dificuldade = 100
            dif_nome = "Média"
            dif_aceita += 1
            intervalo = "1 e 100"
        elif(dif == "d" or dif == "D"):
            dificuldade = 1000
            dif_nome = "Difícil"
            dif_aceita += 1
            intervalo = "1 e 1000"
        else:
            print("Valor inválido!\n")
    print(f"\nDificuldade escolhida: {dif_nome}\n")

    #Sorteando o número e definindo o número de tentativas(sempre será uma a menos que o número digitado se "for" for usado)
    sorte = random.randint(1,dificuldade)
    tentativas = 6
    print("Sorteando o número!\n")
    time.sleep(2)

    # Uso do "for" para o looping sequenciado de acordo com o número de tentativas
    for rodada in range(1, tentativas):
        print("Tentativa {} de {}".format(rodada, tentativas - 1))
        chute = int(input("Digite o seu número: "))

        # Intervalos permitidos
        if (dif == "f" or dif == "F"):
            if (chute < 1 or chute > 10):
                print(f"\nVocê deve digitar um número entre {intervalo}.\n")
                continue
        elif (dif == "m" or dif == "M"):
            if (chute < 1 or chute > 100):
                print(f"\nVocê deve digitar um número entre {intervalo}.\n")
                continue
        elif (dif == "d" or dif == "D"):
            if (chute < 1 or chute > 1000):
                print(f"\nVocê deve digitar um número entre {intervalo}.\n")
                continue

        # Valores
        correto = chute == sorte
        maior = chute > sorte
        menor = chute < sorte

        if(correto):
            print("Parabéns, você acertou! \n")
            break
        elif(maior):
            print("Você errou! O seu chute foi maior que o número secreto \n")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto \n")

    # Finalização
    if(correto):
        print("Fim do jogo.")
    else:
        print(f"Fim de jogo, infelizmente não foi dessa vez, o número era: {sorte}.")
    input("\npressione enter")

if(__name__ == "__main__"):
    play()