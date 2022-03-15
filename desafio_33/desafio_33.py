import os 

precos = []
itens = []

def add_item(n, v):
    itens.append(n)
    precos.append(v)

def del_item(i):
    itens.pop(i)
    precos.pop(i)

def show_lista():
    for x in range(len(itens)):
        print(itens[x],":", "R$", precos[x])

again = 1

while(again != 0):

    print("Lista de Compras :")
    print("")
    print("Escolha uma das opções abaixo :")
    print("1 - Adicionar item e valor;")
    print("2 - Apagar item por index")
    print("3 - Mostrar lista")
    print("4 - Fechar")

    choice = int(input("Digite a opção escolhida : "))

    if(choice == 1):

        nome = input("Digite o nome do item : ")
        valor = input("Digite o valor do item : ")

        add_item(nome, valor)

        print("Você deseja :", "1 - Voltar pro menu", "2 - Fechar")
        option = int(input("Digite a opção escolhida : "))

        if(option == 2):
            again = 0

    elif(choice == 2):

        index = int(input("Digite o index do item a ser apagado"))

        del_item(index)

        print("Você deseja :", "1 - Voltar pro menu", "2 - Fechar")
        option = int(input("Digite a opção escolhida : "))

        if(option == 2):
            again = 0

    elif(choice == 3):

        print("A lista atualmente está :")

        show_lista()

        print("Você deseja :", "1 - Voltar pro menu", "2 - Fechar")
        option = int(input("Digite a opção escolhida : "))

        if(option == 2):
            again = 0

    elif(choice == 4):
        again = 0

    else:

        print("O número que voce escolheu não existe nas opções tente denovo...")


os.system('pause')