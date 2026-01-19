from datetime import date
atual=date.today().year
nascimento=int(input("Digite seu ano de nascimento: "))
idade = atual-nascimento
print(f"O atleta tem {idade} anos")
if idade <= 9:
    print("Sua classificação é mirim")
elif idade <=14:
    print("Classificação: infantil")
elif idade<=19:
    print("Classificação Junior")
elif idade <= 25: 
    print("Classificação Sênior")
else: 
    print("Classificação Master")