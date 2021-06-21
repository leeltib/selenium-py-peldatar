# Írj programot, ami kiírja a kisbetűket, és melléjük az ASCII kódjukat!
# A kiírás több oszlopos legyen, és legfeljebb 10 soros.


column = int(input("3 vagy 4 oszlopban szeretnéd látni a listát? "))

print("------ Megoldás lista használat nélkül ----------------------")

if column == 3:
    for i in range(8):
        szam = i + 97
        print(chr(szam), ":", szam, "   ", chr(szam + 8), ":", szam + 8, "   ", chr(szam + 16), ":", szam + 16)
elif column == 4:
    for i in range(6):
        szam = i + 97
        print(chr(szam), ":", szam, "   ", chr(szam + 6), ":", szam + 6, "   ", chr(szam + 12), ":", szam + 12, "   ", chr(szam + 18), ":", szam + 18)
else:
    print("Rossz számot adtál meg!")


print("------ Megoldás (létrehozott) betűsoros listával --------------------")

szamsor = range(200)
szakasz = list(szamsor[97:123])
abc = []
for i in szakasz:
    abc.append(chr(i))

print(szakasz)
print(abc)
print("-" * 70)

if column == 3:
    for i in range(8):
        print(abc[i], ":", ord(abc[i]), "   ", abc[i+8], ":", ord(abc[i+8]), "   ", abc[i+16], ":", ord(abc[i+16]))
elif column == 4:
    for i in range(6):
        print(abc[i], ":", ord(abc[i]), "   ", abc[i+6], ":", ord(abc[i+6]), "   ", abc[i+12], ":", ord(abc[i+12]), "   ", abc[i+18], ":", ord(abc[i+18]))
else:
    print("Rossz számot adtál meg!")





