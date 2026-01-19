num=int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão: 
      [1]converter para binario
      [2] converter para octal
      [3]converter para hexadecimal''')
opção= int(input("Sua opção: "))
if opção == 1:
    print(f"{num} convertido para binario é igual a {bin(num)[2:]}")
elif opção == 2:
    print("{} convertido para octal é igual a {}".format(num, oct(num)[2:]))
elif opção==3:
    print("{} convertido para hexadecimal é igual a {}".format(num, hex(num)[2:])),
else:
    print("opção invalida")