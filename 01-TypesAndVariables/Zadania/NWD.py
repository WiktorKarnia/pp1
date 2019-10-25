import math
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
print ("Najwiekszy wspólny dzielnik tych liczb to: " ,end="")
print(math.gcd(a, b))