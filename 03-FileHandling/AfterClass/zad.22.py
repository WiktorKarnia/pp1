with open ("C:/Users/user/Desktop/pp1/03-FileHandling/students.txt","r") as file:
    next(file)
    for line in file:
        x = line.split(",")
        if int(x[2]) < 30:
            print(x[0], x[1], x[4])