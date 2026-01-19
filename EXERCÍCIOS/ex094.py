'''
Docstring para EXERCÍCIOS.ex94.py
crie um programa que leia nome, idade e sexo de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todas os 
dicionários em uma lista. No final, mostre: 
a) quantas pessoas foram cadastradas 
b) a média da idade do grupo 
c) uma lsita com todas as mulheres 
d) uma lista com todas as pessoas com idade acima da média
# usar listas e dicionários, while e if 
'''
pessoas = [] # para armazenar os dicionários
dados = {} # para armazenar os dados temporários

soma_idade = 0 
while True: 
    dados.clear() # limpar
    dados['nome'] = str(input("Nome:"))
    while True: # validação do sexo
        dados['sexo'] = str(input('Sexo [M/F]:')).upper()[0]
        if dados['sexo'] in 'MF': 
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    dados['idade'] = int(input('Idade:'))
    soma_idade += dados['idade'] # somar a idade
    pessoas.append(dados.copy()) # copia dos dados
    while True:
        r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if r  in 'SN': 
            break
        print('ERRO! Responda apenas com S ou N.')
    if r == "N":
        break

print('-='*30)
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")
media = soma_idade / len(pessoas)
print(f" B) A média de idade é de {media:5.2f} anos.")
print("C) As mulheres cadastradas foram ", end='')
for p in pessoas: 
    if p['sexo'] == 'F': 
        print(f"{p['nome']}, ", end='')
print()
print("D)  As pessoas com a idade acima da média são ", end= '')
for p in pessoas: 
    if p['idade'] >= media:
        print ('    ', end='')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print('<<<< ENCERRADO >>>>')