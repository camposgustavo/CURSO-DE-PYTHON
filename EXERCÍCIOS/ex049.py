num=(int(input('digite um número para ver sua tabuada:')))
print("_"*13)
for c in range(1,11):
    tabuada=num*c
    print(f"{num}x{c}={tabuada}")
print("_"*13)
print("end")