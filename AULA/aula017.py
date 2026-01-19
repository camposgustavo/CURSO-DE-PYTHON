'''num = [2, 5, 9, 1]
num[2] = 4 
num.append(3)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num: 
    num.remove(5)
else: 
    print("Não achei o número 4")
print(num) 
print(f"Essa lista tem {len(num)} elementos.")'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # enumerate mostra o índice e o valor
    print(f"Na posição {c} encontrei o valor{v}...")
print('Cheguei ao final da lista.')'''

'''valores = []
for cont in range (0,5): 
    valores.append(int(input("Digite um valor: ")))
for c, v in enumerate(valores): # enumerate mostra o índice e o valor
    print(f"Na posição {c} encontrei o valor {v}!")
print('Cheguei ao final da lista.')'''

a = [2,3,4,5]
#b = a # tem uma ligação direta com a, ou seja, se alterar b, altera a também
b = a[:] # cópia da lista a para b, ou seja, se alterar b, não altera a
b[2] = 8
print(f'Lista a: {a}')
print(f'Lista b: {b}')