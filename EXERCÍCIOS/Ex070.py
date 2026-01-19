cont = tot = caro = menor = 0
barato = ''
while True: 
    prod=str(input("Nome do produto: "))
    valor=float(input("Preço: R$"))
    cont +=1
    tot += valor
    if valor > 1000: # é quantos produtos são maior que mil conto
        caro += 1
    if cont == 1 : #or preco < menor: 
        menor = valor 
        barato = prod
    '''else: 
        if valor < menor: 
            menor = valor
            barato = prod'''
    continuar = ' ' # condição de parada 
    while continuar not in 'SN': # enquanto a resposta nã otiver dentro de SN
        continuar = str(input("Deseja Continuar [S/N]?")).strip().upper()[0]
    if continuar == 'N': 
        break
print(f"O total da compra foi R$ {tot}")
print(f"Temos {caro} produtos custando mais de R$1.000,00 ")
print(f"O produto mais barato foi {barato} que custa RS{menor:.2f} ")

# Preciso contar os valores e somar para entregar o total da compra 
# preciso de um if para comparar os valores 
# e mais um para mostrar quais produtos ultrapassaram 1.000