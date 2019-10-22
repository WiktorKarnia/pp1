x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, 2x / y is ", 2*x/y)
elif x < y:
    print("y is smaller")
else:
    print("y is smaller")
print("thanks!")