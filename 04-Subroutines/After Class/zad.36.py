tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
num = []
def integer():
    for i in tab:
        x = isinstance(i,int)
        if x == True:
            num.append(i)
            y = sum(num)
    return y
print(integer())
    

            