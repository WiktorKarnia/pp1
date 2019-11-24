import math
def pierwiastki():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))
    delta = int((b**2)-(4*a*c))
    if delta<0:
        print("Delta mniejsza niz zero, brak pierwiastków.")
    elif delta==0:
        print("Delta równa zero, jeden pierwiastek równy:",(-b)/(2*a))
    else:
        xjeden = ((-b)-(math.sqrt(delta)))/(2*a)
        xdwa = ((-b)+(math.sqrt(delta)))/(2*a)
        print("Delta wieksza niz zero, dwa pierwiastki:",xjeden,",",xdwa)

