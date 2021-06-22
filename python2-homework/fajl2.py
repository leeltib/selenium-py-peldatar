# 026 Feladat: filekezelés gyakorlása / 2

with open("adat.txt", "r") as f:
    rows = f.readlines()
#    print(rows)

szoveg = ""
for row in rows:
    szoveg += row.strip() + " "

print(szoveg)

