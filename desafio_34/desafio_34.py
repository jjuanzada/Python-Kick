import os

vogais = 0

nome = "desafio_34/when_i_was_your_man.txt"

arquivo = open(nome, "r")
texto = arquivo.read()

for x in range(len(texto)):
    
    if texto[x] == "a" or texto[x] == "A" or texto[x] == "e" or texto[x] == "E" or texto[x] == "i" or texto[x] == "I" or texto[x] == "o" or texto[x] == "O" or texto[x] == "u" or texto[x] == "U":
        vogais += 1

arquivo.close()

print("A quantidade de vogais é igual a : ", vogais)
os.system("pause")