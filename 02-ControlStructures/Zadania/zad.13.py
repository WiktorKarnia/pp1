x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
if x>0 and y>0:
    print("Pierwsza ćwiartka")
elif x>0 and y<0:
    print("Czwarta ćwiartka")
elif x<0 and y>0:
    print("Druga ćwiartka")
elif x<0 and x<0:
    print("Trzecia ćwiartka")