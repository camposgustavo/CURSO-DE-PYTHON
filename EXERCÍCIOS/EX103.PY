"""
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA
DOIS PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU. 
O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM~
DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE.
"""

def ficha(nome, gols): 
    if nome == "": 
        nome = "<desconhecido>"
    elif gols == "": 
        gols = "0"
    print(F"O jogador {nome} fez {gols} gol(s) no campeonato.")

nome = str(input("Nome do Jogador: ")).strip()
gols=str(input("Número de gols: ")).strip()
ficha(nome, gols)