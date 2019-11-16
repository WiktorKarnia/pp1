def fib():
    a,b = 0,1
    print(a)
    print(b)
    for i in range(19):
        a,b = b,a+b
        print(b)
    return b
print("20 wyraz to: ",fib())