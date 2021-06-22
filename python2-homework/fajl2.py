# 026 Feladat: filekezelés gyakorlása / 2

with open("adat.txt", "r") as f:
    rows = f.readlines()
#    print(rows)

text1 = ""
for row in rows:
    text1 += row.strip() + " "

print(text1)

