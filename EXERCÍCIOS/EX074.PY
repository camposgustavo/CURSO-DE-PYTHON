'''Crie um programa que vai garar cinco números aleatórios e colocar em uma tupla.
Depois disso. mostre a listagam de números gerados e também indique o menor e o maior valor que estão na tupla.'''

import random 
numeros = (random.randint(1,10), random.randint(1,10) , random.randint(1,10), random.randint(1,10), random.randint(1,10))
print(f"Números gerados: {numeros}")
print(f"O menor número gerado foi: {min(numeros)}")
print(f"O maior número sorteado foi : {max(numeros)}")
