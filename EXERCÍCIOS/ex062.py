primeiro=int(input("Digite o primeiro termo:  "))
razao=int(input("Digite a razão: "))
termo = primeiro # recebe o valor de primeiro
cont= 1 #contador
total = 0
mais = 10
while mais != 0: #aninhados
    total = total + mais 
    while cont <= total: 
        print(f"{termo} → ", end='')
        termo += razao #atribui ao termo
        cont +=1 # conta até ser <= 10
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"progressão finalizada com {total} termos mostrados")
