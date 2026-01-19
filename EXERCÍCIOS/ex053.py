
frase=str(input('Digite uma palavra: ')).strip().upper() #remove os espações e deica maiuscula
palavra = frase.split() # vai fatiar em pedaços e joga em uma lista
junta= ''.join(palavra)

print(f"a palavra {junta} ao contrario é: {junta[::-1]}", end=' ')
if junta == junta[::-1]:
    print("É um palindromo", end=' ')
else: 
    print("Não é um palindromo", end=' ')


'''
Resolução do professor

frase=str(input('Digite uma palavra: ')).strip().upper() #remove os espações e deica maiuscula
palavra = frase.split() # vai fatiar em pedaços e joga em uma lista
junta= ''.join(palavra)
inverso = ''

for letra in range (len(junto) - 1, -1, -1): # vai ler ao contrario
    inverso += junto[letra]
if inverso == junto: 
    print("Temos um palindromo")
else: 
    print("A frase digitada Não é um palindromo")
'''