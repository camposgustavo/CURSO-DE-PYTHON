'''
FAÇA UM PROGRAMA QUE TENHA UMA 
FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES DE UM 
TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE 
A ÁREA DO TERRENO. 
'''

def área(comprimento, largura): 
    a = comprimento*largura
    print(f"A área de um terreno {comprimento} x {largura} é de {a}.")


#programa principal
print(" Controle de Terreno  ")
print('-'*40)
compri=float(input("Insira o comprimento do terreno (m): "))
largu=float(input("Insira a largura do terreno(m): "))
área(compri, largu)
