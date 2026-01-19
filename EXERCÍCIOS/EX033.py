primeiro=int(input("Digite o primeiro valor:"))
segundo=int(input("Digite o segundo valor:"))
terceiro=int(input("Digite o terceiro valor: "))
'''if primeiro<segundo and primeiro<terceiro:
    menor=primeiro
if segundo<terceiro and segundo<primeiro:
    menor=segundo
if terceiro<primeiro and terceiro<segundo:
    menor=terceiro'''
#Qual é o menor
menor = primeiro
if segundo<primeiro and segundo<terceiro:
    menor = segundo
if terceiro<primeiro and terceiro<segundo: 
    menor = terceiro
#Qual é o maior 
maior = primeiro
if segundo>primeiro and segundo>terceiro:
    maior=segundo
if terceiro>primeiro and terceiro>segundo:
    maior=terceiro
print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")