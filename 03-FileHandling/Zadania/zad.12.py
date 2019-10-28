produkt = str(" ")
with open("ShoppingList.txt" , "a") as file:
    while len(produkt) != 0:
        produkt = str(input("Podaj produkt: "))
        file.write(produkt + "\n")
    
    
