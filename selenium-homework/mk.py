# megoldás for ciklussal
for i in range(26):
    szam = i + 97
    print(szam, chr(szam))


# ha szeretnéd listába rendezni, és onnan kiírni:
szamsor = range(200)
szakasz = list(szamsor[97:123])
print(szakasz)
for i in szakasz:
    print(i)


for i in range(8):
    szam = i + 97
    print(chr(szam), ":", szam, "   ", chr(szam + 8), ":", szam + 8, "   ", chr(szam + 16), ":", szam + 16)

