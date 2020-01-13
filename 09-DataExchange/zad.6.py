a = input("Podaj a: ")
b = input("Podaj b: ")
assert b!=0,'Wartość b równa 0!'
assert type(a) == int and type(b) == int, "Wartość a lub b nie jest całokwita"
print(f'{a}/{b} = {a/b}')