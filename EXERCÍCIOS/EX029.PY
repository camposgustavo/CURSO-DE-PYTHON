vel=float(input("Digite a velocidade atual do carro km/h: "))
if vel > 80:
    print("!MULTADO! Você excedeu a velocidade permitida que é de 80km/h")
    multa=(vel-80)*7
    print(f"Você deve pagar de multa: {multa:.2f}")
print("Dirija com segurança!")