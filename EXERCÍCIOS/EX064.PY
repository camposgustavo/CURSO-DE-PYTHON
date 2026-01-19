#Vários numeros 
num= cont = soma = 0
num = int(input("Digite um numero: [999 para PARAR]:"))
while num != 999:
    soma += num
    cont += 1 # contador = contador + 1
    num = int(input("Digite um numero: [999 para PARAR]:")) #repetir o comando para não pegar a flag
print(f"você digitou {cont} numeros e a soma entre eles foi {soma}")
   