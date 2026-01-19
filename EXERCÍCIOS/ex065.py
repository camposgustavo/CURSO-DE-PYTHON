resp = "Ss"
soma = media = quant = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1: # condção para saber qual é o maior e qual é o menor 
        maior = menor = num
    else: 
        if num > maior: 
            maior = num 
        if num < menor: 
            menor = num
    resp=str(input("Quer continuar[S/N]?")).upper().strip()
media = soma / quant
print(f"Você digitou {quant} numeros e a média dos valores digitados é: {media}")
#print(f"A soma dos valores:{soma}")
print(f"O maior número foi {maior} e o menor foi {menor}")
print("Acabou")