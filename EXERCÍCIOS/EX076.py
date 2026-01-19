# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços.
#na sequência.
#No final, mostre uma listagem de preços. organizando os dados em forma tabular.

Listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, "Caneta", 2.00, 'Marcador', 3.00)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(Listagem)): # percorre toda a tupla 
    if pos % 2 == 0: # verifica se a posição é par
        print(f'{Listagem[pos]:.<30}', end='') # imprimi o nome do produto
    else:
        print(f'R$ {Listagem[pos]:>7.2f}') # imprimi o preço 
print('-' * 40)

# a questão foi usar impar e par para separar os nomes dos preços
