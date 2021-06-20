# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
# Írja ki ezek után a beolvasott számok összegét!

number = int(input("Írj ide egy tetszőleges számot: "))
number_sum = [0]

while True:
    if number < 10 and sum(number_sum) >= 100:
        print(f"Gratulálok, elérted a 100 pontot!")
        break
    elif number < 10 and sum(number_sum) < 100:
        number_sum.append(number)
        number = int(input("Kérem a következő számot: "))
    else:
        print("Rossz szám, a játékod véget ért.")
        print(f"Most {sum(number_sum)} pontot értél el. A cél 100 pont!")
        print("Próbálj rájönni a szabályra!")
        break
