sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'FfmM':
    sexo = str(input("Dados Invalidos, tente novamente,Digite o sexo: ")).strip().upper()[0]
print (sexo)