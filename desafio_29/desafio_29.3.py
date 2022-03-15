print("Cadastro de produto")

nome = str(input("Digite o nome do produto : "))
price = float(input("Digite o preço(sem sifrão) : "))
cod = int(input("Digite o código do produto(sem espaços, pontos e traços) : "))
qtd = int(input("Digite a quantidade : "))

print("O produto", nome, "(de código : ", cod, ") tem ", qtd, "em estoque no valor de : R$", price)