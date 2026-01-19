while True:
    num=(int(input('digite um número para ver sua tabuada:')))
    if num < 0 : 
        print("Programa Tabuada ENCERRADO! Obrigada.")
        break
    for c in range(1,11):
        tabuada = num * c
        print(f"{num}x{c}={tabuada}")
    print("="*40)