
totf=0 # contador
velho=0 
conta = 0 
idades = 0
nome_velho= ""
for i in range (1,5):
    print(f"-----{i}º pessoa-----")
    nome=str(input("nome: "))
    idade=int(input("idade: "))
    sexo=str(input("Sexo [M/F]: ")).strip().upper()
    if sexo == "F":
        if idade < 20: 
            totf += 1
    elif sexo == "M":
        if idade > velho: 
            velho = idade 
            nome_velho = nome
conta += 1
idades += idade
média =(idades/conta)
print(f"A média de idade do grupo é de {média} anos")
print(f"Ao total {totf} mulheres têm menos de 20 anos ")
print(f"O nome do homem mais velho é {nome_velho} e ele tem {velho} anos")