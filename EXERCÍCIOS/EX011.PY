
lar = float(input("Qual a largura da parede?"))
alt = float(input("Qual a altura da parede?"))
al=lar*alt
lt=al/2
print("Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².".format(lar,alt, al))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(lt))