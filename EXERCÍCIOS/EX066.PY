n = s = c = 0 
while True: 
    n = int (input("Digite um valor (999 para parar): "))
    if n == 999: # Condição de parada
        break
    c += 1 #Conta quantos números foram digitados
    s += n #Soma
    
print(f"Foram digitados {c} e a soma é {s}")