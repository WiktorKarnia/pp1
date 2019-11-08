imiona = ["Wiktor", "Adam","Julia", "Marcin", "Weronika"]
def jestImie(imie,imiona):
    imie = input("Imie: ")
    if imie in imiona:
        result = "Imie jest zawarte w wykazie imion."
    else:
        result = "Imie nie jest zawarte w wykazie imion."
    return result
print("Imiona: ",imiona)
print(jestImie("",imiona))
