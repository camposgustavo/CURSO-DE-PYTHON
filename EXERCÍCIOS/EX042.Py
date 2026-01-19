p1=float(input("Primeiro lado:"))
p2=float(input("Segundo lado: "))
p3=float(input("Terceiro lado: "))

if p1<p2+p3 and p2<p1+p3 and p3<p1+p2:
    print("Podem formar um triângulo ")
    if p1==p2 and p2==p3:
        print("O triangulo é Equilatero")
    elif p1 != p2 != p3 !=p1:
        print("O triângulo é Escaleno")
    else: 
        print("O triângulo é Isósceles")
else: 
    print("Os segmentos acima NÃO formam um triângulo ")

