'''Crie um programa onde o usuário digite uma expressÃO qualquer que use parenteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.'''

pilha = [] # serve para armazenar os parenteses abertos
expre = str(input('Digite a expressao: '))
for pare in expre: # percorrer cada item da expressao 
    if pare == '(': # se for um parenteses aberto
        pilha.append('(') # adiciona na pilha
    elif pare == ')': # se for um parenteses fechado
        if len(pilha) > 0: # se a pilha tiver algum item
            pilha.pop() # remove o ultimo item 
        else: # se a pilha estiver vazia
            pilha.append(')') # adiciona um parenteses fechado
            break
if len(pilha) == 0: # se a pilha estiver vazia
    print("Sua expressão está correta")
else: 
    print('Sua expressão está incorreta')