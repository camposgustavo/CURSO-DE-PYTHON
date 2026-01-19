# dicionarios 

pessoas = {'nome': 'Tecna', 'sexo': 'F', 'idade': 23 }
#print(pessoas)
#print(pessoas['nome'])
#print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys()) # mostra as chaves (nome, sexo, idade)
#print(pessoas.values())# mostra os valores (tecna, 22, f)
#print(pessoas.items()) # mostra os dois juntos
#acessando por laçõs 
'''for k in pessoas.keys(): # laço para acessar as chaves
    print(k)

for k in pessoas.values(): # laço para acessar os valores
    print(k)

for k, v in pessoas.items(): # laço para acessar os dois juntos
    print(f'{k} = {v}')'''

'''pessoas['nome'] = 'Nera' #alterando valor da chave nome
#adicionando 
pessoas['peso'] = 62.3
#del pessoas['sexo'] # deleta o item sexo 
for k, v in pessoas.items(): # laço para acessar os dois juntos
    print(f'{k} = {v}')'''

# dicionario dentro de uma lista 

'''brasil = [] # ou list()
estado1= {'uf': 'Rio de Janeiro', 'sigla': 'RJ'} # dicionarios
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1) 
brasil.append(estado2)
#print(estado2) 
print(brasil)
print(brasil[0]) # acessando pimeiro estado
print(brasil[1]) # acessando o segundo estado
print(brasil[0]['uf']) # acessando valor da uf do 1 estado
print(brasil[1]['sigla'] ) # aceesando valor da silga do 2 estado'''

estado = dict () # ou {}
brasil = list() # ou []

for c in range(0,3): 
    estado['uf'] = str (input("Unidade Federativa: "))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    #brasil.append(estado [:]) # tem que copiar o dicionario, não é uma relação, é uma cópia e não serve [:]
    brasil.append(estado.copy()) # metodo interno de dicionarios para copiar
#print(brasil)

'''for e in brasil: 
    #print(e)
    for k, v in e.items(): 
        print(f"O campo {k} tem valor {v}")'''

for e in brasil: # percorre cada dicionario dentro da lista brasil
    for v in e.values(): # percorre os valores de cada dicionario
        print(v, end=' ')
    print()