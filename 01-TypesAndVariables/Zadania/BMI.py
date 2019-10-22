print("Podaj swoją wagę w kg: ")
x=float(input())
print("Podaj swój wzrost w cm: ")
y=float(input())
z= x/(y/100)**2
print(z)
if z>=8.5 and z<=24.99:
    print("Waga prawidłowa")
else:
    print("Waga nieprawidłowa")