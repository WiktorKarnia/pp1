tab = [15,38,7,23,14]
x = 23
def check(tab,x):
    print(f'Liczba:', x)
    print(f'Tablica: ', tab)
    for i in tab:
        i = int(i)
        if x == i:
            print("Liczba jest w tablicy.")
       