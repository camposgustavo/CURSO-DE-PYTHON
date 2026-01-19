massa=float(input("peso (KG): "))
altura=float(input("altura (M): " ))
imc = massa / ( altura ** 2)
print("O imc é de:{:.1f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
else:  # imc >= 40
    print("Obesidade mórbida, cuidado!")