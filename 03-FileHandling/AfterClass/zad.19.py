list = []
with open ('C:/Users/user/Desktop/pp1/03-FileHandling/universities.txt','r') as file:
    for line in file:
        list.append(line)
        list.sort()    
        with open ('C:/Users/user/Desktop/pp1/03-FileHandling/universities.txt','w') as file:
            for x in list:
                file.write(x)
        