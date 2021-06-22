# 026 Feladat: filekezelés gyakorlása / 3

with open("adat.txt", "r") as f:
    rows = f.readlines()
#    print(rows)

szoveg = ""
for row in rows:
    szoveg += row.strip() + " "
print(szoveg)

with open("adat2.txt", "w") as f2:
    f2.write(szoveg)

# ellenőrzés:

with open("adat2.txt", "r") as f3:
    row2 = f3.readline()
    print(row2)

