'''Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol na ordem de 
colocação. Depois mostra:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense/Santos.'''
print('='*60)
print('{:^60}'.format("Tabela do Campeonato Brasileiro de Futebol 2024"))
print('='*60)
times = ('Flamengo', 'Internacional', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos', 'Corinthias', 'Vasco da Gama', 'Internacional', 'Ceará SC', 'Fortaleza', 'Juventude', 'Sport Recife')
print(f'Os 5 primeiros colocados são: [{times[0:5]}]') # fatiamento da tupla para mostrar os 5 primeiros
print(f'Os 4 últimos colados são: [{times[-4:]}] ') # fatiamento da tupla para mostrar os 4 últimos
print(f'Times em ordem alfabética: {sorted(times)}') # sorted() organiza os times em ordem alfabética
print(f'O time da Santos está na {times.index("Santos")}ª posição.') # index() mostra a posição do time Santos

