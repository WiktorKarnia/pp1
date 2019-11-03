with open ("C:/Users/user/Desktop/pp1/03-FileHandling/numbersinrows.txt","r") as file:
    for line in file:
        x = line.split(",")
        y = len(x)
        