dias=int(input('Quantos dias foi alugado?'))
kms=float(input('Quantos km rodado?'))
pago= dias*60 + (kms*0.15)
print("O total a pagar é de R${:.2f}".format(pago))