#eu tava certooooo
n1=int(input("Digite o primeiro termo:  "))
r=int(input("Digite a razão: "))
d=n1+(11-1)*r
for c in range (n1,d, r):
    print(f"{c} ", end='→ ')
print("Acabou")
