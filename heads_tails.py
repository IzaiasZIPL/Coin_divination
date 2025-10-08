import random 
from time import sleep
import sys

options = ["Cara", "Coroa"]

print('Bem vindo a divinação com moedas!\n\nFaça a sua pergunta, tente ser o máximo específico para que a moeda entenda sua pergunta e o ajude!\nNão abuse muito, tente um melhor de três para cada pergunta.\n')

question = input("Digite sua pergunta, para que a moeda o responda! ")

CoinSide = input("Qual lado da moeda equivale a sim? Digite Cara ou Coroa: ")

def best_of_three(): 
    while(True):
        if CoinSide == "cara":
            print("Cara é \"sim\", coroa é \"não\".")
            print(question)
            sleep(3)
            print(random.choice(options))
            print(random.choice(options))
            print(random.choice(options))
            
            option = input("Deseja continuar? sim/não: ")

            if option == "sim":
                continue
            elif option == "não":
                sys.exit()         
        else:
            print("Coroa é \"sim\", cara é \"não\".")
            print(question)
            sleep(3)
            print(random.choice(options))
            print(random.choice(options))
            print(random.choice(options))    
            
            
            option = input("Deseja continuar? sim/não: ")

            if option == "sim":
                continue
            elif option == "não":
                sys.exit()    
    
    
            
while True:
    option_bestof3 = input("Deseja ir o modo normal ou um melhor de três(Você receberá o resultado de três moedas e a que se repetir mais de uma vez é a resposta correta)?\nDigite \"modo normal\" ou \"melhor de tres\".\nSe deseja parar a divinação digite \"não\". ")
    
    if option_bestof3 == "modo normal":
        print(question)
        sleep(1)
        if CoinSide == "cara":
            print("Cara é \"sim\", coroa é \"não\".")
            print(question)
            sleep(3)
            print(random.choice(options))
            
            option = input("Deseja continuar? sim/não: ")

            if option == "sim":
                continue
            elif option == "não":
                break

        else:
            print("Coroa é \"sim\", cara é \"não\".")
            print(question) 
            sleep(3)
            print(random.choice(options))

            option = input("Deseja continuar? sim/não: ")

            if option == "sim":
                continue
            elif option == "não":
                break
    elif option_bestof3 == 'melhor de três' or 'melhor de tres':
        best_of_three()
        
    elif option_bestof3 == 'não' or 'nao':
        sys.exit()
    
    else: 
        print('digite uma resposta válida')
        continue
