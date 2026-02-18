"""Crie um programaque tenha a função LEIAINT(), que vai funcionar 
de forma semelhante á função input() do python, só que fazendo a 
validação para aceitar apenas um valor númerico.
Ex: n = leiaint('Digite um n: ')
"""

def leiaint(msg): 
    while True: 
        n = str(input(msg))
        if n.isnumeric(): # verfica se o valor é um número
            return int(n) # retorna o valor convertido para inteiro
        else: 
            print("ERRO!Por gentileza, digite um número inteiro válido.")


# Programa Principal 
n = leiaint("Digite um número: ")
print(f" Você acabou de digitar o número {n}")