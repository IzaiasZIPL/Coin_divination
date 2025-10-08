import random 
from time import sleep

options = ["Cara", "Coroa"]

print('Bem vindo a divinação com moedas!\n\nFaça a sua pergunta, tente ser o máximo específico para que a moeda entenda sua pergunta e o ajude!\nNão abuse muito, tente um melhor de três para cada pergunta.\n')

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
                break
            
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
                break
        
    pass

while True:
    question = input("Digite sua pergunta, para que a moeda o responda! ")
    
    CoinSide = input("Qual lado da moeda equivale a sim? Digite Cara ou Coroa: ")
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
