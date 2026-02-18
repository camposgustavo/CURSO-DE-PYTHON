# FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO 
# TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO. NO FINAL, MSOTRE O 
# CONTEÚDO NA TELA

aluno = {} # dicionario aluno 
aluno['nome'] = str(input('Nome do Aluno: ')) # adiciona o nome do aluno
aluno['media'] = float(input(f'Média de {aluno["nome"]}:')) # calcula a média
if aluno['media'] >= 7:  # verifica
    print(f"Situação é igual a APROVADO")
else: 
    print(f"Situação é igual a REPROVADO")
