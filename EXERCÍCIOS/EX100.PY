'''
Docstring para EXERCÍCIOS.EX100

Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''

from random import randint 
from time import sleep

def sorteia(lista): 
    print("Sorteando 5 valores da lista: ", end='')
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f" {n} ", end='', flush=True)
    print()

def somaPar(lista): 
    count = 0
    soma = 0
    for valor in lista: # verifica se o numero é par
        if valor % 2 == 0:
            soma += valor
    print(f'Somando o valores pares de {lista} temos {soma}.')

numeros=[]
sorteia(numeros)
somaPar(numeros)