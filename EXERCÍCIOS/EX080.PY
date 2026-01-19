
'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort(0). No final, mostra a lista ordenada na tela'''

num = [] # cria a lista vazia
for cont in range(0,5): 
    num.append(int(input("Dgite um valor:")))
    for posicao in range (0, len(num)-1): # percorre a lista até a penulitma posiçao
        if num [-1] < num[posicao]: # compara o ultimo vlor com os outros
            num.insert(posicao, num[-1]) # insere o valor
            num.pop()# remove o ultimo valor que está duplicado
            break
print(f"Os valores digitados em ordem foram: {num}")