'''help()
print(input.__doc__) '''
#docstrings 
'''
 são como etiquetas que colocamos no código Python para descrever o que uma função, classe ou módulo faz.
'''


'''def contador (i, f,p): 
    """
    Faz uma contagem e mostra na tela.
    :param i: Início da Contagem.
    :param f: Fim da Contagem.
    :param p: Passa a contagem.
    :return: sem retorno.

    Função criada por Gustavo Campos estudante de Cieência da Computação.
    """
    c = i # 1, conta os impares
    while c <= f: 
        print(f"{c}", end='..')
        c += p
    print('Fim!'''


#contador(2,10,2) # parametro formal
#contador(0,100,10) # vai de 0 até 100, pulando de 10 em 10
#help(contador)


'''def somar(a=0,b=0,c=0): #c, conhecido com parametro opcional, informa ou não (=0)
    """
    Docstring para somar
    
    Faz a soma de trÊs valores e mostra o resultado na tela:
    :param a: O primeiro valor.
    :param b: O segundo valor.
    :param c: O terceiro valor.
    Função criada por Gustavo Campos estudante de Ciência da Computação.
    """
    s = a+b+c
    print(f'A soma vale {s}.', end='')

somar(3,2,5)
somar(8,4) # pode nomear os parametros
somar() # parametros opcionais
somar(3, 3, 5, 4) # usar multipos parametros'''


#ESCOPO DE VARIÁVEIS


'''def teste(): 
    x = 8 # escopo local, funciona apenas na região do df
    print(f'Na Função teste, n vale {n}.')
    print(f'Na Função teste, x vale {x}.')


# Programa Principal
n = 2
print(f"No programa principal, n vale {n}.")
teste()
print(f"No programa principal, x vale {x}")'''


# escopo global


'''
#escopo global
def teste(b): 
    global a # ele não vai criar uma variavel a
    a = 8
    b+=4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f"C dentro vale {c}.")


a = 5
teste(a)
print(f"     A fora vale {a}.")
print(f"    B fora vale {b}.")
print(f"    C fora vale {c}.")
'''


# RETORNANDO VALORES

def somar(a=0, b=0, c=0): 
    s= a + b + c
    #print(f"A soma vala {s}.")
    return s

#resp = somar(3, 2, 5) # ou dentro de um print
r1 = somar(3,2,5)
r2 = somar(1,7)
r3=  somar(4)
print(f"Meus cálculos deram {r1}, {r2} e {r3}.")

