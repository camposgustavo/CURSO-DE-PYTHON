"""
Fça um programa que tenha uma função notas() que pode receber 
várias notas de alunos e vai retonar um dicionário com as seguintes
informações: 
- Quantidade de notas
- A maior nota
- A menor nota 
- A média da turma 
- A situação (opcional)

Adicione também as docstrings da função.
"""


def notas(resp, sit = False): 
 r = { }
 r['TOTAL'] = len(resp)
 r['MAIOR'] = max(resp)
 r['MENOR'] = min(resp)
 r['MÉDIA'] = sum(resp) / len(resp)
 if sit == True: 
  if r['MÉDIA'] >= 7:
   r['SITUAÇÃO'] = 'BOA'
  elif r['MÉDIA'] >=5: 
   r['SITUAÇÃO'] = "RUIM"
  else: 
   r['SITUAÇÃO'] = "PÉSSIMA"



# PROGRAMA PRINCIPAL 
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)