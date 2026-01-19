# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista unica
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# verificar o codigo do exercício 082 
numeros = [[], [], []] # primeira lista numeros, a segunda pares e a terceira impares
#gambiarra chick
while True: # também pode ser feito com for
    n = int(input("Digite um valor: "))
    numeros[0].append(n) 
    if n % 2 == 0: 
        numeros[1].append(n)
        numeros[1].sort() # ordena a lista de pares
    else: 
        numeros[2].append(n)
        numeros[2].sort() # impares e ordena
    r = str(input("Quer continuar? [S/N]")) # condição de parada
    if r in 'Nn': 
        break 
print(f"Os valores pares digitados foram: {numeros[1]}")
print(f"Os valores impares digitados foram: {numeros[2]}")
