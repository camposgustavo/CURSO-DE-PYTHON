# CRIE UMA PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE
# TUDO EM UMA LISTA COMPOSTA. NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA
# ALUNO E PERIMITA QUE O USUÁRIO POSSAR MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE. 
# fiz baseado no exerciico 084
notas=[]
numeros= []
dados= []
while True:
    dados.append(str(input("Nome do aluno: ")))
    dados.append(float(input("Nota 1: [usar ponto ao invés de vírgula]")))
    dados.append(float(input("Nota 2:")))
    notas.append((dados[1] + dados[2]) / 2)
    numeros.append(dados[:]) # adiciona uma cópia dos dados na lista 
    dados.clear()
    r = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
    if r == "N":
        break
print("-="*30)
print(f"{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}") # :< serve para alinhar à esquerda 
print("-="*30)
for i in range(0, len(numeros)): 
    print(f"{i:<}{numeros[i][0]:<10}{notas[i]:>8.1f}")
    while True: 
        opc = int(input("Mostrar notas de qual aluno? (999 para parar)")) 
        if opc <= len(numeros) -1: # o -1 indica o último índice da lista
            print(f"Notas de {numeros[opc][0]} são {numeros[opc][1]} e {numeros[opc][2]}")
        if opc == 999: # parar
            print("FINALIZANDO...")
            break