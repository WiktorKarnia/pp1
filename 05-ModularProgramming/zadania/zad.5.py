import statistics
kwoty = [21600, 4350, 3920, 5590, 3250, 4010]
def mean(kwoty):
    sr = statistics.mean(kwoty)
    return sr
print(mean(kwoty))


def mediana(kwoty):
    kwoty.sort()
    med = statistics.median(kwoty)
    return med
print(mediana(kwoty))


def standard_devation(kwoty):
    kwoty.sort()
    st_dev = statistics.pstdev(kwoty)
    return st_dev
print(standard_devation(kwoty))

