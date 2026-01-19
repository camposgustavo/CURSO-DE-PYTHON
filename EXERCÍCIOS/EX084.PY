# FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA.
# NO FINAL, MOSTRE:
# A) QUANTAS PESSOAS FORAM CADASTRADAS.
# B) UMA LISTA COM AS PESSOAS MAIS PESADAS.
# corrigir o código para que funcione conforme o enunciado
pessoas = []
dados = []
while True: 
    dados.append(str(input("Nome: "))) 
    dados.append(float(input("Peso: "))) 
    pessoas.append(dados[:])
    dados.clear()
    r = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if r == "N": 
        break
print(f"Foram cadastradas {len(pessoas)} pessoas.")
for p in pessoas: 
    if p[1] >= 80: 
         print(f"{p[0]} é mais pesada que 80kg.")
    else: 
        print(f'{p[0]} não é mais pesada que 80kg.')