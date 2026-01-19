import math
ang=float(input("Digite um Ângulo:"))
seno=math.sin(math.radians(ang))
cosseno=math.cos(math.radians(ang))
tangente=math.tan(math.radians(ang))
print("O ângulo de {} tem o seno de {:.2f}".format(ang, seno))
print("O ângulo de {} tem o cosseno de {:.2f}".format(ang,cosseno))
print("O ângulo de {} tem a tangente de {:.2f}".format(ang,tangente))