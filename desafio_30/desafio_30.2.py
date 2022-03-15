print("Calcula média")

a = float(input("Digite a sua altura : "))
p = float(input("Digite o seu peso : "))
imc = float

imc = p/(a*a)

print("Seu IMC é : ", imc)

if imc<=18.5:
    print("Você está na categoria : magreza")
elif imc>18.5 and imc<=24.9:
    print("Você está na categoria : normal")
elif imc>=25 and imc<=29.9:
    print("Você está na categoria : sobrepeso")
elif imc>=30 and imc<=39.9:
    print("Você está na categoria : obesidade")
else:
    print("Você está na categoria : obesidade grave")
