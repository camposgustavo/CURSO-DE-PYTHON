maior =0 
menor = 0
for pe in range (1, 6):
    peso = float(input(f"peso da {pe} º pessoa: "))
    if pe == 1: 
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior=peso
            if peso < menor:
                menor = peso
print ("o maior peso foi {}kg e o menor peso foi de {}kg".format(maior, menor))