import os

y = int(input("Digite um número: "))

for i in range(1,y):
    if i%2 != 0:
        print(i)

os.system('pause')