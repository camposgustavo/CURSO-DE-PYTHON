"""
Docstring para EXERCÍCIOS.EX099

Faça um programa que tenho uma função 
chamada maior(), que receba vários parâmetros com valores
inteiros. 

seu programa tem que analisar todos os valores e dizer qual deles é  maior. 
"""

def maior(* núm): # desempacotador
    cont = maior = 0 
    print("\n analisando os valores recebidos")
    for valor in núm: 
        print(f"{valor} ", end=' ')
        if cont == 0: 
            maior = valor
        else: 
            if valor > maior:
                 maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo. ")
    print(f"O maior valor inserido foi {maior}")
       # print(f"O menor numero foi {min(valor)}")


# programa principal

maior(2, 3, 4, 5, 6, 9, 8)
maior (4, 7, 0)
maior (2,6)
maior(9)
maior (0)