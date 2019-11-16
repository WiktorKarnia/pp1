import random
print("Dla 1000 liczb losowych z przedziału <1,50>:")
tab = []
podz = []
notpodz = []
for i in range (0,1000):
    tab.append(random.randrange(1,50))
def even():
    for i in tab:
        if i%2 == 0:
            podz.append(i)
    result = (len(podz)/1000)*100
    return result
print("Liczby parzyste to: ",even(),"%")
def noteven():
    for i in tab:
        if i%2 != 0:
            notpodz.append(i)
    result = (len(notpodz)/1000)*100
    return result
print("Liczby nieparzyste to: ",noteven(),"%")