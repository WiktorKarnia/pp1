x = 8050
y = int(input("Podaj kod PIN: "))
if x != y:
    print("PIN niepoprawny.")
    y = int(input("Podaj kod PIN: "))
if x != y:
    print("PIN niepoprawny.")
    y = int(input("Podaj kod PIN: "))
if x != y:
    print("Karta zostaje zablokowana.")
else:
    print("Zaakceptowano.")