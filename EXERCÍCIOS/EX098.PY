'''
Docstring para EXERCÍCIOS.EX098

faça uma programa que tenha uma função chamada contador(), 
que receba três parâmetros: inicio, fim e passo e realize a contagem. 

seus programa tem que realizar três contagens através da função criada: 

a) De 1 até 10, de 1 em 1 
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
'''
from time import sleep
def contador(a, b, c):
    if c < 0: 
        c *= -1
    if c == 0: 
        c = 1

    print(f"Contagem de {a} até {b} de {c} em {c}.")
    
    if a < b:
        cont = a
        while cont <= b: 
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont += c
        print("fim")
    else: 
        cont = a
        while cont >= b:
            print(f"{cont}", end=' ', flush=True)
            sleep(0.3)
            cont -= c
        print("FIM")


contador(1,10,1)
contador(10,0,2)
print("You´re ready? É sua vez de personalizar a contagem. ")
inicio=int(input("Digite o inicio: "))
fim=int(input("Digite o Fim: "))
passo=int(input("Digite o passo: "))
contador(inicio, fim, passo)