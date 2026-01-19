from datetime import date
atual=date.today().year
totme=0
totma=0
for pess in range (1,8):
    nasc=int(input("Em que ano a {}º pessoa nasceu?" .format(pess)))
    idade=atual-nasc
    if idade >= 21: 
        print("Essa pessoa é maior")
        totma += 1 #para contar quantas pessoas já atingiram a maior idade
    else:
        print("Essa pessoa é menor") 
        totme += 1 #para contar quantas pessoas ainda não atingiram a maior idade
print("{} pessoas não atingiram a maior idade". format(totme))
print("{} pessoas já atingiram a maior idade". format(totma))