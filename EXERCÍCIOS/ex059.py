n1=int(input("Digite o primeiro valor: "))
n2=int(input("Digite o segundo valor: "))
opcao=0
while opcao != 5:
    print(''' 
      [1] somar 
      [2] multiplcicador 
      [3] maior
      [4] novos números
      [5]sair do programa''')
    opcao=int(input("Escolha a opção: "))
    if opcao == 1: 
        s=n1+n2
        print(s)
    elif opcao == 2: 
        m=n1*n2
        print(m)
    elif opcao == 3: 
        if n1> n2:
            maior = n1 
        else: 
            maior = n2 
        print ("O numero maior é; {}".format(maior))
    elif opcao == 4: 
        n1=int(input("Digite o primeiro valor: "))
        n2=int(input("Digite o segundo valor: "))
    elif opcao == 5: 
        print("Finalizando...")
    else: 
        print('opção invalida')

print("Fim do progama! Volte sempre!")