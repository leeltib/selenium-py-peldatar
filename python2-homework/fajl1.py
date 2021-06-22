# 026 Feladat: filekezelés gyakorlása / 1

with open("adat.txt", "r") as f:
    row_num = len(f.readlines())

text1 = ""
with open("adat.txt", "r") as f:
    for i in range(row_num):
        row = f.readline()
        text1 += row.strip() + " "

print(text1)

