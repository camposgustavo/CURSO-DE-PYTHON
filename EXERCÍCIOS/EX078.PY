'''Faça um programa que leia 5 valores numéricos a guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado a as suas respectivas posições na lista.'''

# melhorar para mostrar todas as posições do maior e menor valor caso haja repetição

num = [] # cria a lista vazia
for cont in range(0,5): 
    num.append(int(input("Dgite um valor:")))
print(f'Você digitou os valores {num}')
print(f"O menor número gerado foi: {min(num)} e sua posição é: {num.index(min(num))}")
print(f"O maior número sorteado foi : {max(num)} e sua posição é: {num.index(max(num))}")

# 

'''if min'''