preco = float(input('Qual é o preço do produto? R$'))
desc=preco-(preco * 5 /100)
print('O valor do produto com 5% de desconto é: R${:.2f}'.format(desc))