import math
a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))
p = 0.5*(c*b*a)
P = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Pole tego trójkąta to: ",end="")
print(P)