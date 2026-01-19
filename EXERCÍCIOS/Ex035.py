print("-----------------------------")
print(" ANALISADOR DE TRIÂNGULOS ")
print("-----------------------------")
p1=float(input("Primeiro lado:"))
p2=float(input("Segundo lado: "))
p3=float(input("Terceiro lado: "))

if p1<p2+p3 and p2<p1+p3 and p3<p1+p2:  # se o p1 for menor que o p2 somado com o p3 e …

    print("Podem formar um triângulo ")
else: 
    print("Os segmentos acima NÃO formam um triangulo ")