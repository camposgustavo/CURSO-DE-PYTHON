from random import randint
computador=randint(0,10) #faz o computador sortear um número de 0 a 10
print("vou pensar em um numero de 0 a 10. Consegue adivinhar? ")
acertou = False
palpite= 0
while not acertou: 
    jogador=int(input("Em que número pensei? "))
    palpite += 1
    if jogador == computador:
        acertou= True
    else: 
        if jogador < computador: 
            print("mais")
        elif jogador > computador:
            print("menos")
print("Acertou e você teve {} palpites".format(palpite))
