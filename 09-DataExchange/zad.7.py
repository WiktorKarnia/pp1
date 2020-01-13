waga = float(input("Podaj wage: "))
wzrost = int(input("Podaj wzrost: "))
assert type(waga) == float, "Waga źle zapisana."
assert type(wzrost) == int, "Wzrost źle zapisany."
assert waga >= 40.0 and waga <= 150.0, "Niepoprawna waga."
assert wzrost >= 150 and wzrost <= 220, "Niepoprawny wzrost."
BMI = (waga/(wzrost/100)**2)
BMI = str(BMI)
print("Twoje BMI to " + BMI)
