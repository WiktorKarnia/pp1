list = []
with open ('C:/Users/user/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for x in file:
        if int(x)%2==0:
            list.append(x)
        else:
            continue
with open ('evennumbers.txt','x') as file:
    for y in list:
        file.write(y)
    