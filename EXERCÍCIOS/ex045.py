from random import randint 
itens =("Pedra", "Papel", "Tesoura")
computador= randint(0,2)
print('''opções: 
      [0]Pedra
      [1]Papel
      [2]Tesoura''')

jogador=int(input("Qual a sua escolha?"))
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))

if computador == 0:
      if jogador == 1: 
            print("Jogador vence")
      elif jogador == 2:
            print("Computador vence")
      else: 
            print("Jogada invalida")
elif computador == 1: 
      if jogador == 0: 
            print("Computador vence")
      elif jogador == 2:
            print("Jogador vence")
      else: 
            print("Jogada invalida")
elif computador == 2:
      if jogador == 1: 
            print("computador vence")
      elif jogador == 0:
            print("Jogador vence")
      else: 
            print("Jogada invalida")
elif computador == jogador: 
      print("Empate")