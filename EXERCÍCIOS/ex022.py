'''nome=str(input('Digite seu nome completo:'))#.strip()#(remover espaçõs)
print("Seu nome em maiúscula é: {}".format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print("Seu nome tem {} letras.".format(len(nome),nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))'''

nome=str(input('Digite seu nome completo:'))#.strip()#(remover espaços)
print(f"Seu nome em maiúscula é: {nome.upper()}") #Deixa tudo em maiúscula
print('Seu nome em minúsculas é: {}'.format(nome.lower())) #Deixa tudo em minúscula
print("Seu nome tem {} letras.".format(len(nome)-nome.count(' '))) #conta 
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #conta 



