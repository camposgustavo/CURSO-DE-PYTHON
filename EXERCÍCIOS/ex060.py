'''from math import factorial
n=int(input("Digite um número: "))
f=factorial(n)
print("O fatorial é: {}".format(f))'''
'''num=int(input("Digite um numero:" ))
fatorial = 1
x=1
while x <= num:
    fatorial= fatorial * x
    x += 1
print(fatorial)'''

n = int(input("Digite um número para calcular seu fatorial: "))
c = n 
f = 1 #pode importar da biblioteca math o fatorial 
print(f"Calculando {n}! = ", end='')
while c > 0: 
    print(f"{c}", end='')
    print(" X " if c > 1 else " = ", end='')
    f *= c
    c -= 1
print(f"{f}")