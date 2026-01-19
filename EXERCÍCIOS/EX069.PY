totf=0 #contador para as mulheres
conti = 0#contador para a idade
toth = 0 # contador para homens
while True: 
    print("----Cadastro ----")
    idade=int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input("Sexo [M/F]: ")).strip().upper()[0]
    if idade >= 18: 
        conti += 1
    if sexo == "F" and idade < 20:
            totf += 1
    if sexo == "M":
        toth += 1      
    continuar = ' '
    while continuar not in 'SN':
        continuar = (input("Deseja Continuar [S/N]?")).strip().upper()[0]
    if continuar == 'N': 
        break
print(f"Total de pessoas com mais de 18 anos {conti}")
print(f"Total de mulheres com menos de 20 anos {totf}")
print(f"Temos {toth} homens cadastrados")


