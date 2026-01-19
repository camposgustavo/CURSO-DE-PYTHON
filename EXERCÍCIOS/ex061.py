primeiro=int(input("Digite o primeiro termo:  "))
razao=int(input("Digite a razão: "))
termo = primeiro # recebe o valor de primeiro
cont= 1 #contador
while cont <= 10: 
   print(f"{termo} → ", end='')
   termo += razao #atribui ao termo
   cont +=1 # conta até ser <= 10
print("Fim")