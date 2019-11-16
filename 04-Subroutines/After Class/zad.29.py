tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
tab.sort()
def mediana():
    tab.sort()
    x = len(tab)
    y = int(x/2)
    result = (tab[y] + tab[y-1])/2
    return result
print(mediana())
