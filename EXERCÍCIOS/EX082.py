'''Crie um programa qua vai ler vários números a colocar em uma lista.
Depois disso. Crie duas listas extras que vão conter apenas os valores pares e os valores imparas digitados.
respectivamente.Ao final, mostre o conteúdo das três listas garadas.'''

numeros = []
pares = []
impares = [] 

while True: 
    n=int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0: # verifica se é par
        pares.append(n)
    else: # é impar
        impares.append(n)
    r = str(input("Quer continuar? [S/N]"))
    if r in "Nn": 
        break
print(f"A lista completa é: {numeros}")
print(f"A lista de pares é: {pares}")
print(f"A lista de impares é: {impares}")