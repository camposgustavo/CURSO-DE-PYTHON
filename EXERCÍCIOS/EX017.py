import math
cat1=float(input("Digite o cateto oposto:"))
cat2=float(input("Digite o cateto adjacente:"))
hipotenusa= math.hypot(cat1, cat2)
print("A hipotenusa vai medir:{:.2f}".format(hipotenusa))