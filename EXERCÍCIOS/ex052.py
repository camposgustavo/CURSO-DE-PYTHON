n1=int(input("Digite um número: "))
tot = 0 #para saber o numero de divisivel 
for c in range(1, n1 +1): # para c no intervalo de 1 até o numero digitado# o for conta 1 a menos
    if n1 % c == 0: # se o modulo da divisão entre n1 e c for igual a zero
        print("divisivel por ", end='' )
        tot += 1 #tot = tot + 1
    else: 
        print("não divisivel por ",end='' )
    print(f'{c} ',) #end pula linha 
print(f"O número {n1} foi divisível {tot} vezes", )
if tot==2:
    print("Ele é um número primo")
else :
    print("Não é um número primo")