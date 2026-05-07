"""
Exercício 106 
faça um mini sistema que utilize o interactive Help do Python,
O usuário vai digitar o comando e o manual vai aparecer. Quando o 
usuário digitar a palavra 'Fim', o programa se encerrará. OBS: Use cores
"""

#Fazer um dicionario de cores
cores = ('\033[m',          #0 - sem cores
         '\033[0;30;41m',   #1 - vermelho
        '\033[0;30;44m',    #2 - azul
        '\033[0;30;45m',    #3 - roxo
        '\033[7;30m'        #4 - branco
         );

def ajuda (com): 
    título(f"Acessando o manual do comando \'{com}\'", 1)
    help(com)

def título (msg, cor=0): 
    tam = len(msg) + 4 
    print(cores[cor], end='')
    print('>' * tam) 
    print(f'  {msg}') 
    print("<" * tam)
    print(cores[0], end='')

# Programa principal 
comando = ''

while True: 
    título('Sistema de ajuda PyHelp', 2)
    comando = str(input("Função ou Biblioteca : //"))
    if comando.upper() == "FIM":
        break 
    else:
        ajuda(comando)
título("Busque o caminho do conhecimento", 3)