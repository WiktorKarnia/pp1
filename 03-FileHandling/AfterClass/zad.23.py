import re
suma = 0
list = []
thing = "\\d"
with open("C:/Users/user/Desktop/pp1/03-FileHandling/land.txt", "r") as file:
    x = re.findall(thing, file.read())
    for a in x:
        a = int(a)
        suma = suma + a
print (suma) 