print("-"*30)
print("Sequência de Fibonacci")
print("-"*30)
n=int(input("Quantos termos você quer mostrar?"))
t1 = 0 #termo 1
t2 = 1 #termo 2
print(f'{t1} → {t2}', end="")
cont = 3 #conta a partir do 3
while cont <= n: 
    t3 = t1 + t2 #terceiro termo
    print(f" → {t3}", end="")
    t1=t2 #PARA CONTINUAR A SEQUENCIA E IR PULANDO
    t2=t3
    cont += 1
print(" → fim")
