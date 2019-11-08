def Suma(n):
    result = 0
    if n == 0 or n == 1:
        return n
    else:
        for i in range(1, n + 1):
            result += i
    return result        
print(Suma(0))