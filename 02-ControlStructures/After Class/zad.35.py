import math
a = input('Podaj a: ')
b = input('Podaj b: ')
c = input('Podaj c: ')
print(f'Funkcja: {a}x^2 + {b}x + {c}')
delta = int(b)**2 - (int(4) * int(a) * int(c))
if delta < 0:
    print("Funkcja nie posiada pierwiastków.")
elif delta == 0:
    print("Funkcja ma jeden pierwiastek: x= " ,end="")
    x = -(int(b))/(2*int(a))
    print(x)
else:
    print("Funkcja ma dwa pierwiastki: x= " ,end="")
    y = (-(int(b))-(math.sqrt(delta)))/(2*int(a))
    print(int(y) ,end="")
    print( " i x = " ,end="")
    z = (-(int(b))+(math.sqrt(delta)))/(2*int(a))
    print(int(z))