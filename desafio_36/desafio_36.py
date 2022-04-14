import os, requests, openpyxl
from bs4 import BeautifulSoup

print("\n")

again = 1

planilha = openpyxl.Workbook()
page = planilha['Sheet']
page.title = 'cidades'   
page.append(['Cidade', 'Info'])
planilha.save("Cidades-Pesquisadas.xlsx")

page.column_dimensions['A'].width = 20
page.column_dimensions['B'].width = 200

def traz_info_cidade(c):
    
    cidade.replace(" ", "_")

    url = requests.get('https://pt.wikipedia.org/wiki/'+cidade)
    content = url.content

    site = BeautifulSoup(content, 'html.parser')

    div = site.find('div', attrs={'class': 'mw-parser-output'})
    p = div.find('p')
    texto = p.text

    if p:

        print("\n"+" - "+texto+"\n")

        page.append([cidade, texto])

    else:
        
        print("Verifique os acentos e as maiúsculas e tente novamente!!")

    planilha.save("Cidades-Pesquisadas.xlsx")

while(again != 0):

    print("Cidades na Wikipédia"+"\n")
    print("Escolha uma das opções abaixo :"+"\n")
    print("1 - Buscar informações da cidade;")
    print("2 - Fechar"+"\n")

    choice = int(input("Digite a opção escolhida : "))
    print("\n")

    if(choice == 1):

        cidade = input("Digite a cidade : ")
        print("\n"+"Sobre a "+cidade+" :"+"\n")

        traz_info_cidade(cidade) 

        print("Você deseja :", "1 - Voltar pro menu", "2 - Fechar")
        option = int(input("Digite a opção escolhida : "))

        if(option == 2):
            again = 0

    elif(choice == 2):
        again = 0

    else:

        print("O número que voce escolheu não existe nas opções tente denovo...")


os.system("pause")