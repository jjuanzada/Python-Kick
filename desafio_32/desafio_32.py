import os

def calcula(x1, x2, f):
    if f == 1:
        r = x1 + x2;
        print("a soma dá : ")
        print(r)
    elif f == 2:
        r = x1 - x2;
        print("a subtração dá : ")
        print(r)
    elif f == 3:
        r = x1 * x2;
        print("a multiplicação dá : ")
        print(r)
    elif f == 4:
        r = x1 / x2;
        print("a divisão dá : ")
        print(r)
    else:
        print("o número da operação é inválido");

n1 = int(input("digite o primeiro número : "))
n2 = int(input("digite o segundo número : "))
print("as opções da calculadora são : ")
print("1 = soma")
print("2 = subtração")
print("3 = multiplicação")
print("4 = divisão")
o = int(input("digite o numero da operação desejada : "))

calcula(n1, n2, o)

os.system('pause')