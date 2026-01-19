# Crie um programa que leia nome, ano de nascimento e 
# carteira de trabalho e cadastre-os (com idade) em um dicionário.
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
#anos de aposentaria = 35 anos de contribuição
# 

from datetime import date
trabalhador = {}
atual = date.today().year
trabalhador['nome'] = str(input('Nome:'))
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
trabalhador['idade'] = idade
trabalhador['ctps'] = int(input("Carteira de Trabalho (0 não tem): ")) 
if trabalhador ['ctps'] != 0: 
    trabalhador ['contratação'] = int(input('Ano de contratação: '))
    trabalhador ['salario'] = float(input('Salário R$: '))
    anos_para_aposentar = trabalhador['contratação'] + 35 - nascimento
    aposentadoria = idade + (trabalhador['contratação'] - nascimento)
    trabalhador ['idade aposentadoria'] = aposentadoria
    trabalhador ['anos para aposentar'] = anos_para_aposentar
print('-='*30)
for k, v in trabalhador.items(): 
    print(f"{k} tem o valor {v}") # mostra a chave e o valor do dicionario 

