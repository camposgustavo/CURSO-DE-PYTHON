# crie um programa onde 4 jogadores joguem um dado e tenham resultadods aleatórios 
# guarde esses resultados em um dicionario. no final, coloque esse dicionario em ordem. 
# sabendo que o vencedor tirou o maior número no dado. 
#biblioteca tempo para fazer as pausas
import time 
import random 

print('-='*30)
jogo = {} # dicioanario para guardar os resultados 
for c in range(1,5): # loop para os jogadores
    jogo[f'jogador {c}'] = random.randint(1,6) # sorteia o num entre 1 e 6 
    print(f"O jogador {c} tirou {jogo[f'jogador {c}']} no dado.")
print('-='*30)
#colocando em ordem 
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True) # ordena o dicionario pelo valor (item[1]) do maior para o menor (reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking): # percorre a lista com índice #enumerate para pegar o índice e o valor 
        print(f"{i+1}º lugar: {v[0]} com {v[1]}.")
print('-='*30)
