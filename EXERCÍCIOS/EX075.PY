'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final mostra:
A) Quantas vezes apareceu o valor 9 .
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

# preciso fazer a correção do código abaixo
# preciso armazenar 4 valores diferentes em uma tupla 
# consigo usar count() para contar quantas vezes o valor 9 apareceu?
count = 0
valores = ()

valores = valores + (int(input('Digite um número: ')),)
valores = valores + (int(input('Digite outro número: ')),)
valores = valores + (int(input('Digite mais um número: ')),)
valores = valores + (int(input('Digite o último número: ')),)

print(f"Os valores digitados foram : {valores}")

count_9=valores.count(9) # count serve para contas quantas vezes um valor aparece
print(f"O valor 9 apareceu {count_9} vezes.")

if 3 in valores: 
    print(f"O valor 3 apareceu na {valores.index(3)+1}ª posição.") # o index mostra a posição
else: 
     print("O valor 3 não foi digitado")

for valor in valores: # verifica se o numero é par
        if valor % 2 == 0:
            count += 1
print(f'Os valores pares digitados foram: {count} ', end='')
    