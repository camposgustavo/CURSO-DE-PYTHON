
# passando por parametro 
'''def mensagem (msg): 
    print ('--------------------')
    print (msg)
    print ('--------------------')

mensagem( 'sistema de alunos')'''


'''def titulo (txt): 
    print('-' * 30) 
    print(txt)
    print('-' * 30)

# programa principal 
titulo('    Curso em Video      ')
titulo('    Python é muito bom  ')'''


# exemplos por parâmetros 
'''def soma(a, b):
    print(f'A={a} e B={b}')
    s = a + b
    print(f'A soma A + B = {s}')


# programa principal
soma (4, 5)
soma(8, 9)
soma(2, 1)'''

'''a = 4 
b = 5 
s = a + b 
print(s)
a = 8 
b = 9 
s = a + b 
print(s)
a=2 
b=1
s=a + b
print(s)
'''

# empacotamento 

'''def contador (*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 8)
contador(8, 3)
contador(4, 4, 8, 6, 2 )'''

def dobra  (lst): 
    pos= 0 
    while pos < len(lst):
        lst[pos]*=2
        pos +=1


valores = [2, 6, 5, 0, 3, 8]
dobra(valores) 
print(valores)