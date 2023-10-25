# Importar os outros ".py" e as bibliotecas
import time
import random
import Advinhacao
import Forca

def menu():
    # Seleção do Game
    print("*******************")
    print("Escolha o seu jogo!")
    print("*******************\n")

    print("(1) Advinhação\n(2) Forca\n")

    choice = int(input("\nDigite o número referente ao jogo de sua escolha: "))

    if(choice == 1):
        print("\nAbrindo o Jogo da Advinhação!\n")
        time.sleep(2)
        Advinhacao.play()
    elif(choice == 2):
        print("\nAbrindo o Jogo da Forca!\n")
        time.sleep(2)
        Forca.play()

if(__name__ == "__main__"):
    menu()
