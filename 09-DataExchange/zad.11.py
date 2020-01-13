wiek = input("Podaj swój wiek: ")
if type(wiek) != int:
    raise TypeError('Wiek powinien być liczbą całkowitą!')
if wiek < 0 or wiek > 120:
    raise ValueError("Niepoprawny wiek.")
print(f'Masz {wiek} lat')