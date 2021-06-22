# 026 Feladat: filekezelés gyakorlása / 1

with open("adat.txt", "r") as f:
    row_num = len(f.readlines())

szoveg = ""
with open("adat.txt", "r") as f:
    for i in range(row_num):
        row = f.readline()
        szoveg += row.strip() + " "

print(szoveg)

