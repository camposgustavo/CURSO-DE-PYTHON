print('{:=^40}'.format("804.STUDIO"))
compras=float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO 
      [ 1 ] À VISTA DINHEIRO/CHEQUE
      [ 2 ] À VISTA CARTÃO
      [ 3 ] 2X NO CARTÃO 
      [ 4 ] 3X OU MAIS NO CARTÃO''')
opção=int(input("Escolha a opção: "))
if opção == 1:
    desconto= compras-(compras*10/100)
elif opção == 2:
    desconto= compras-(compras*5/100)
elif opção==3:
    desconto=compras
    parcela = desconto / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif opção==4:
    desconto= compras+(compras*20/100) 
    totparc=int(input("quantas parcelas?"))
    parcela = desconto / totparc
    print("Sua compra será parcelada em {}x de R${:.2f}".format(totparc, parcela))
else:
    print("Opção invalida")
print("Sua compra de  R$ {:.2f} vai custar {:.2f} no final".format(compras, desconto))