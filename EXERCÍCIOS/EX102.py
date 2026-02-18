"""
Docstring para EXERCÍCIOS.EX102
Crie um programa que tenha uma função fatorial () que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial. 
faça a documentaçaõ da função
"""


def fatorial(num, show=False):
    """
    Docstring para fatorial
    fatorial (n, show=False)
    -> Calcula o fatorial de um numero 
    :param n: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n.
    """
    c = num
    f = 1 #pode importar da biblioteca math o fatorial 

    if show == True: 
        while c > 0: 
            print(f"{c}", end='')
            print(" X " if c > 1 else " = ", end='')
            f *= c # multiplica o valor de f por c e armazena o resultado em f
            c -= 1
        print(f"{f}")
    else: 
        while c > 0: 
            f *= c
            c -= 1 
        print(f"O Fatorial de {num} é = {f}")


num= int(input("Digite um número para calcular seu fatorial: "))
teste = input("Deseja mostrar o processo de cálculo? [S/N]").strip().upper()[0]
fatorial(num, show = teste in 'Ss')