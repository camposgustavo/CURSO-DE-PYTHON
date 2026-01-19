# faça um programa que ajude um jogador da mega sena a criar palpites. 
# o programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

import random 

print("-="*30)
print("      JOGO DA MEGA SENA      ")
print("-="*30)

jogos = list()
quant = int(input("Quantos jogos você quer que eu sorteie? "))

for n in range(0, quant):  # para cada jogo 
    jogos=list()
    while True: 
        num = random.randint(1,60) # sorteia um numero entre 1 e 60 
        if num not in jogos: # se o numero não estiver na lista
            jogos.append(num)
        if len(jogos) >= 6: # condição de parada caso a lista tenha 6 numeros
            break
    jogos.sort() # ordena a lista
    print(f"Jogo {n+1}: {jogos}") # printa o jogo
print("-="*30) 
print("         < BOA SORTE! >      ")
print("-="*30)