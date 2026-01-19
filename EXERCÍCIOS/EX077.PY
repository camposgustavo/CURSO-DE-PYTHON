'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar. para cada palavra. quais são as suas vogais.'''

palavras = ('aprender', 'python', 'manga', 'natal', 'recife', 'londres', 'cariri')
#mostrando a posição de cada item 
for cont in range (0, len(palavras)): # usa o range com a função len
    print(f'Na palavra {palavras[cont]} ', end='')
    for letra in palavras[cont]: 
        if letra in 'aeiou': 
            print(letra, end=' ') 
    print()
