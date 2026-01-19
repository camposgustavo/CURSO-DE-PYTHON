from random import randint
computador=randint(0,5) #faz o computador sortear um número de 0 a 5
print("vou pensar em um numero de 0 a 5.")
jogador=int(input("Em que número pensei? "))
if jogador == computador:
    print("parabens, você acertou")
else: 
    print("Ganhei, eu pensei no numero {} e não no {}".format(computador,jogador ))