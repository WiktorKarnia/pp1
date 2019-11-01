import re
list = []
with open ('C:/Users/user/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for line in file:
        list.append(line)
        list.sort()
print(list)