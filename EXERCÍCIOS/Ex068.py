'''from random import randint # biblioteca para gerar numero

while True: 
    computador = randint(0,11) # gera um numero aleatorio 
    jogador=int(input("Digite um valor: "))
    escolha = str(input("Par ou impar? [P/I]"))

    soma=jogador+computador
    resultado = soma % 2
    if resultado == 0: 
            print(f"Você jogou {jogador} e o computador {computador} e o total foi {resultado} ")
    else: 
            print(f"Você jogou {jogador} e o computador {computador} e o total foi {resultado}")'''

from random import randint # biblioteca para gerar numeros 
v=0
while True: 
        computador = randint(0,11) # gera um numero aleat de 0 a 10
        jogador =int(input("Digite um valor: "))
        soma = jogador + computador 
        escolha = ' '
        while escolha not in 'PI': #verifica se um elemento não está presente em uma sequência
                escolha =str(input('Par ou impar [P/I]?')).strip().upper()[0]
        print(f"Você jogou {jogador} e o computador {computador} e o total foi {soma}")
        print('Deu Par' if soma % 2 == 0 else 'Deu Impar')
        if escolha == 'P':
                if soma % 2 == 0: 
                        print("Você venceu!!")
                        v += 1
                else:
                        print( "Você perdeu!")
                        break
        elif escolha == 'I':
                if soma % 2 == 1: 
                        print("Você venceu!")
                        v +=1
                else: 
                        print("Você perdeu!")
                        break
        print("Vamos jogar novamente! ")
print(f"GAY OVER! Você venceu {v} vezes")