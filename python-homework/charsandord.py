# Írj programot, ami kiírja a kisbetűket, és melléjük az ASCII kódjukat!
# A kiírás több oszlopos legyen, és legfeljebb 10 soros.

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]

column = int(input("3 vagy 4 oszlopban szeretnéd látni a listát? "))

if column == 3:
    for i in range(8):
        print(abc[i], ":", ord(abc[i]), "   ", abc[i+8], ":", ord(abc[i+8]), "   ", abc[i+16], ":", ord(abc[i+16]))
elif column == 4:
    for i in range(6):
        print(abc[i], ":", ord(abc[i]), "   ", abc[i+6], ":", ord(abc[i+6]), "   ", abc[i+12], ":", ord(abc[i+12]), "   ", abc[i+18], ":", ord(abc[i+18]))
else:
    print("Rossz számot adtál meg!")

