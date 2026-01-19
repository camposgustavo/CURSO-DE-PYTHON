'''Exercício Python 071: Crie um programa que simule o funcionamento 
de um caixa eletrônico. No início, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print("~~"*30)
print('{:^30}'.format("BANCO SYNAPSE"))
print("~~"*30)

valor=int(input("O valor a ser sacado: R$ ")) #input do valor a ser sacado
sacar = valor

cedula = 50 # maior valor da cédula
totalced = 0 #variável que vai contar o total de cédulas
while True: 
    if sacar >= cedula: # se o total a sacar for maior ou igual a cédula
        sacar -= cedula # subtrai o valor da cédula do total a sacar
        totalced += 1 # conta mais uma cédula
    else: 
        if totalced > 0: # se já tiver contado alguma cédula
            print(f'Total de {totalced} cédulas de R$ {cedula}') 
        if cedula ==50 : # se a cédula for 50
            cedula = 20 # muda para a próxima cédula
        elif cedula == 20: 
            cedula = 10 
        elif cedula == 10: 
            cedula = 1 
        totalced = 0
        if sacar == 0: 
            break 
print("~~"*30)

