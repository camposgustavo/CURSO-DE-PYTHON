celcius = float (input("Informe a temperatura em °C: "))
f= ((9*celcius)/5)+32 #ordem de precedenci, se anarlisar não é necessaerio os parenteses 
k= ((5*celcius)/5)+273
print("A temperatura de {}°C corresponde a {}°F".format(celcius, f))
print("A temperatura de {}°C corresponde a {}°k".format(celcius, k))