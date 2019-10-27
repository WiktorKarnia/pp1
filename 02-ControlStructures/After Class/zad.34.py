p = input("Podaj numer pesel: ")
k = ['0', '2', '4', '6', '8']
list(p)
if len(p) != 11:
    print("Pesel niepoprawny.")
else:
    if p[9] in k:
        print("Płeć: Kobieta")
    else:
        print("Płeć: Mężczyzna")
    if p[2] in ['2' , '3']:
        print("Wiek: " ,end="")
        w = 2018 - (2000 + int(p[0:2]))
        print(w)
    else:
        print("Wiek: " ,end="")
        w = 2018 - (1900 + int(p[0:2]))
        print(w)