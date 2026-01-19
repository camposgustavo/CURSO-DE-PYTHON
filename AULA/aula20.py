'''def lin(): # rotina "comando novo"
    print('-'*30)


#programa principal
lin()
print(' CURSO EM VÍDEO  ')
lin()
print(' APRENDA PYTHON  ')
lin()
print(' GUSTAVO CAMPOS  ')
lin()'''

'''#parâmetros 

def titulo(txt): 
    print('-='*30)
    print(txt)
    print('-='*30)


#principal
titulo(' CURSO EM VÍDEO  ')
titulo(' APRENDA PYTHON  ')
titulo(' GUSTAVO CAMPOS  ')'''


'''
PARTE PRATICA
'''

'''def soma(a, b): 
   print(f'A = {a} e B= {b}')
   s = a + b
   print(f'A soma vale A + B = {s}')


#programa principal
soma(b=4, a=5) # passando parametro
soma(8, 2) # passando parametro'''
'''soma(4, 5)
soma (8, 9)
soma(2, 1)
soma(4, 1)'''

# empacotar parametros
'''def contador(* num): # * serve para desempacota
    #for valor in num:
        #print(f'{valor} ', end='')
    #print("FIM!")
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números.")

contador(2, 1, 7)
contador(0, 0)
contador(4, 4, 7, 6, 2)'''

'''# com listas 
def dobra(lst): # a função dobra recebe uma lista
    pos = 0
    while pos < len(lst): # enquanto a psoição for menor do qu o tamanho da çista
        lst[pos] *= 2
        pos +=1

valores=[7, 2, 5, 0, 4]
dobra(valores)
print(valores)'''

def soma( * valores): 
    s = 0
    for num in valores: 
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)