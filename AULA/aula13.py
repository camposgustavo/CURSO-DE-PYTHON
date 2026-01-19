'''for c in range (0, 6): #ele não considera o ultimo numero ou seja se você quer 6 tem que ser 7
    print("Oi")
print("Fim")'''

'''for c in range (0, 6):
    print(c)
print('fim')'''

'''for c in range (6, 0, -1):
    print(c)
print('fim') # de tras para frente(3,2,1..)'''

'''for c in range (0,15, 2): #de 0 até 7 pulando de 2 em 2
    print(c)
print('fim')'''

'''n=int(input("Digite um número: "))
for c in range (0,n+1):
    print(c)
print('Fim')'''

'''i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range (i, f+1, p):
    print(c)
print("FIM")'''

s = 0
for c in range (0,3): 
    n = int(input("Digite um valor: "))
    s += n
print("o somatório é: {}".format(s))