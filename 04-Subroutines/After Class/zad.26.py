x = int(input("Podaj dochód: "))
def tax(x):
    if x<5000:
        y = x * 0.17
        result = f'Należny podatek: {y}'
    else:
        y = (5000*0.17)+((x-5000)*0.32)
        result = f'Należny podatek: {y}'
    return result
print(tax(x))