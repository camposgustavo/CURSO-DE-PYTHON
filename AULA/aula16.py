'''pode iniciar com (tuplas), [listas] ou {dicionários}'''

'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Acarajé', 'Açaí')
#print(lanche)

print(sorted(lanche)) # mostra a tupla em ordem alfabética sem alterar a tupla original'''

'''#Tuplas São IMUTÁVEIS
# sempre ignora o ultimo elemento 
print(lanche[2]) # Acessando o item na posição 2 
print(lanche[-3]) # Acessando o item na posição -3 (contagem reversa)
print(lanche[1:3]) # Acessando do índice 1 até o 2 
print(lanche[2:]) # Acessando do índice 2 até o final
print(lanche[:2]) # Acessando do início até o índice 1 
print(lanche[-3:]) # Acessando do índice -3 até o final

#lanche[1] = 'Refrigerante' # tuplas são imutáveis, não aceitam atribuição 

for cont in range (0, len(lanche)): # usa o range com a função len
    print(f'Eu vou comer {lanche[cont]}')
print("Larica vegan")


print(len(lanche))

for comida in lanche: # usa a variavel composta
    print(f'Eu vou comer {comida}')
print('Eu tava era amarrado!')

#mostrando a posição de cada item 
for cont in range (0, len(lanche)): # usa o range com a função len
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print("Larica vegan")

for pos, comida in enumerate(lanche): # usa a variavel enumerate (pesquisar) 
    print(f"Eu vou comer {comida} na posição {pos}" )'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # concatenação de tuplas
print(c)
print (len(c)) # conta quantos elementos tem
print(c.count(5)) # conta quantas vezes o valor 5 aparece na tupla
print(c.index(8)) # mostra a posição do valor
print(c.index(5, 1)) # mostra a posição do valor 5, começando a busca na posição 1, chama de deslocamento'''

pessoa = ('Margaret', 69, 'F', 65) # aceita vários tipos de dados
#del(pessoa) # apaga a tupla inteira, del serve para qualquer coisa dentro do python
print( pessoa)
#não tem como deletar um elemento específico da tupla