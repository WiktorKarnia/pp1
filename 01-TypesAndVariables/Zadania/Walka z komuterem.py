import random
a = int(input("Podaj ile oczek wyrzucił komputer: "))
b = random.randrange(1,6)
print("Komputer wylosował: " ,end="")
print(b)
print("Zgadłeś: ",end="")
print(bool(a==b))