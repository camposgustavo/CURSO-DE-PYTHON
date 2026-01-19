'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso 
de zero até vinte.
Sau programa deverá lar um número palo taclado (entre 0 a 20) a mostrá-lo por extenso.'''

contagem=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: # cria um loop infinito
    num=int(input('Digite um número entre 0 e 20: ')) # pede ao usuário que insira um número
    if 0 <= num <=20: # if verifica se o número está entre 0 e 20
        break # se o número tiver dentro do intervalo o loop é interrompido
    print('Tente novamente.', end = '') 
print(f"Você digitou o número {contagem[num]}.")