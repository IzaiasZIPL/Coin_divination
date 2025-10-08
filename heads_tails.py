import random 
from time import sleep
import sys

options = ["Cara", "Coroa"]

print('Bem vindo a divinação com moedas!\n\nFaça a sua pergunta, tente ser o máximo específico para que a moeda entenda sua pergunta e o ajude!\nNão abuse muito, tente um melhor de três para cada pergunta se quiser algo mais certeiro.\n')

question = input("Digite sua pergunta, para que a moeda o responda! ")

CoinSide = input("Qual lado da moeda equivale a sim? Digite Cara ou Coroa: ")

def four_coins():
    
    print("Divinação com quatro moedas funciona da seguinte forma:\n uma pergunta com em que a o lado da sua moeda que equivale a \"sim\" aparece:\n nenhuma vez -> definitivamente não\n uma vez -> não\nduas vezes -> indeterminado\ntrês vezes -> sim\nquatro vezes -> definitivamente sim")
    
    while(True):
        if CoinSide == "cara":
            print("Cara é \"sim\", coroa é \"não\".")
            print(question)
            sleep(3)
            print(random.choice(options))
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
            print(random.choice(options))    
            
            
            option = input("Deseja continuar? sim/não: ")

            if option == "sim":
                continue
            elif option == "não":
                sys.exit()    

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
    option_wich = input("Deseja ir o modo normal, melhor de três(Você receberá o resultado de três moedas e a que se repetir mais de uma vez é a resposta correta) ou quatro moedas?\nDigite \"modo normal\", \"melhor de tres\" ou \"quatro moedas\".\nSe deseja parar a divinação digite \"não\". ")
    
    if option_wich == "modo normal":
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
    elif option_wich == 'quatro moedas':
        four_coins()
            
    elif option_wich == 'melhor de três' or 'melhor de tres':
        best_of_three()
        
    elif option_wich == 'não' or 'nao':
        sys.exit()
    
    else: 
        print('digite uma resposta válida')
        continue
