soma = 0
for c in range (0,500,3):
    if c%2!=0 and c%3==0:
        soma += c
print("A soma de todos os números impares e multiplus de 3 entre 1 e 500 é: {}".format(soma))