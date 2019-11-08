def potega(x,n):
    if n == 0 :
        return 1
    elif n == 1:
        return n
    else:
        return x**n
print(f'5 do potęgi 3 to: {potega(5,3)}')