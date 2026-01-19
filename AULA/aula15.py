'''cont = 1
while cont <= 10: #enquanto cont for menor igual 10 faça
    print(cont, ' ', end="")
    cont += 1
print("Acabou")'''

'''cont = 1
while True: #enquanto loop infinito
    print(cont, ' ', end="")
    cont += 1
print("Acabou")''' 

'''n=0
while n != 999:
    n = int(input("Digite um numero: "))'''

'''n= cont = 0
while cont < 3: #le a quantidade de numero 
    n = int(input("Digite um número: "))
    cont += 1'''

'''n = 0
while n != 999: # so para quando for igual a 999 ( o 999 é o flag, é o ponto de parada)
    n = int(input("Digite um número: "))'''

'''#com soma dos valores 
n = s = 0
while n != 999: # so para quando for igual a 999 ( o 999 é o flag, é o ponto de parada) e os números vão ser somados
    n = int(input("Digite um número: "))
    s += n 
s -= 999 #gambiarra chique
print(F'A soma vale {s}.')'''


# interrompendo com flags 
n = s = 0
while True: 
    n = int (input("Digite um número: ")) #entrada
    if n == 999: # quando o numero for igual a 999 ele para e não conta
        break
    s += n # soma 
print(f"A soma vale {s}") #interpolação de strings

