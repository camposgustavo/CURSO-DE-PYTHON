distancia=float(input("Qual a distância da sua viagem em KMs?"))
print("Você está prestes a começar uma viagem de {}km.".format(distancia))
'''if distancia <=200:
    preco= distancia * 0.50
else:
    preco= distancia * 0.45'''
#if simplificado
preco=distancia * 0.50 if distancia<= 200 else distancia * 0.45
print("E o preço da sua viagem será de R${:.2f}".format(preco))  