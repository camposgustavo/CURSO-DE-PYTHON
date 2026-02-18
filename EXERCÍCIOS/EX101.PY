'''
Docstring para EXERCÍCIOS.EX101
Crie um programa que tenha uma função chamada voto ) que vai receber como parâmetro 
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem 
vot NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições.
'''
from datetime import date #captura a data atual do sistema
def voto (ano): 
     data = date.today().year
     idade = data - ano
     if idade < 16: 
          return f'Com {idade} anos : VOTO NEGADO.'
     elif idade >= 18 and idade < 65:
          return f"Com {idade} anos: VOTO OBRIGATÓRIO."
     else: 
          return f"Com {idade} anos: VOTO OPCIONAL."
     
ano = int(input("Digite o ano de nascimento: "))
print(voto(ano))