import random
def rzutkostka(x,y,z):
    return(x+y+z)
x = random.randrange(1,6)
y = random.randrange(1,6)
z = random.randrange(1,6)
print("Wyrzucone oczka: " , x, y, z)
print("Suma oczek: " ,rzutkostka(x,y,z)) 