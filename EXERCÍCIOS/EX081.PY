'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está OU NÃO na lista.'''

numeros = [] 
while True: 
    n=int(input("Digite um valor:"))
    numeros.append(n)
    r = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if r == "N": 
        break 
print(f"Você digitou {len(numeros)} números") # ler a quantidade de numeros
numeros.sort(reverse=True) #  ordem decrescente
print(f"Os valores em ordem decrescente são: {numeros}")
if 5 in numeros: 
    print('O valor 5 faz parte da lista')
else: 
    print('O valor 5 não faz parte da lista')