import os
import random


def numero(difc):
     numcomp = random.randint(1,difc)
     return numcomp
def limpar():
    try:
        os.system('cls')
    except:
        os.system('clear')
def play():
    tentativas = 0
    nundifc = int(input("Sortear numeros entre 1 e: "))
    numcomp = numero(nundifc)
    while True:
        tentativas = tentativas + 1
        try:
            respatf = input("Seu palpite: ")
            respat = int(respatf)
            if respat < numcomp:
                print("Meu numero e mais pra cima!")
                limpar()
            elif respat > numcomp:
                print("Meu numero e mais pra baixo! ")
                limpar()
            if respat == numcomp:
                print("Vc acertou depois de",tentativas,"tentativas :)")
                return
        except:
            print("erro")
def tentardnv():
    resp = input("Deseja tentar novamente? (s/n) ")
    if resp == "s" or resp == "S":
        limpar()
        play()
    if resp == "n" or resp == "N":
        print("Obrigado por jogar, by EznDvlpr")
        exit 
       
play()
print("Vc ganhou")
tentardnv()

