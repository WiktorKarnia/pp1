napis = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
def samogloski(x):
    result = napis.count(x)
    return result
print("A:",samogloski("a"),"razy.")
print("Ą:",samogloski("ą"),"razy.")
print("E:",samogloski("e"),"razy.")
print("Ę:",samogloski("ę"),"razy.")
print("I:",samogloski("i"),"razy.")
print("O:",samogloski("o"),"razy.")
print("U:",samogloski("u"),"razy.")
print("Y:",samogloski("y"),"razy.")