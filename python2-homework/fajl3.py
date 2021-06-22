# 026 Feladat: filekezelés gyakorlása / 3

with open("adat.txt", "r") as f:
    rows = f.readlines()
#    print(rows)

text1 = ""
for row in rows:
    text1 += row.strip() + " "
print(text1)

with open("adat2.txt", "w") as f2:
    f2.write(text1)

# ellenőrzés:

with open("adat2.txt", "r") as f3:
    row2 = f3.readline()
    print(row2)

