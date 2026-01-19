'''teste = list()
teste.append('Gustavo')
teste.append(20)

peoples =list()
peoples.append(teste)
print(peoples'''

'''teste = list()
teste.append('Gustavo')
teste.append(20)

peoples =list()
peoples.append(teste) # precisa criar uma copia
teste[0] = 'Tecna'
teste[1] = 22
peoples.append(teste) # precisa criar uma copia, se não ele referencia o mesmo local na memoria
print(peoples)'''

'''teste = list()
teste.append('Gustavo')
teste.append(20)

peoples =list()
peoples.append(teste[:]) # precisa criar uma copia
teste[0] = 'Tecna'
teste[1] = 22
peoples.append(teste[:]) # precisa criar uma copia, se não ele referencia o mesmo local na memoria
print(peoples)'''

'''galera = [['João',19], ['Tecna', 22], ['Mario', 20], ['Mariane', 18]] # uma lista com varias estruturas
print(galera[0][0]) # acessa o nome do joão
print(galera[2][1]) # acessa a idade do mario 
print(galera[1][0]) # acessa o nome da tecna
for p in galera: 
    print(f"{p[0]} tem {p[1]} anos de idade.")'''

galera = list()
dado = list () 
totmai = totmen = 0
for c in range (0,3): #5
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:]) # cria uma copia da lista dado
    dado.clear() # limpa a lista dado para a proxima iteração 
print(galera)
for p in galera: 
    if p[1] >= 21: 
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else: 
        print(f"{p[0]} é menor de idade.")
        totmen +=1 
print(f"Temos {totmai} maiores de idade e {totmen} menores de idade.")

