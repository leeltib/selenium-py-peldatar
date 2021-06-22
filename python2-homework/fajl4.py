# 026 Feladat: filekezelés gyakorlása / 4

with open("adat.txt", "r") as f:
    rows = f.readlines()
    print(rows)

with open("adat3.txt", "w") as f2:
    for row in rows:
        f2.write(row)



# ellenőrzés/1:

with open("adat3.txt", "r") as f3:
    row2 = f3.readlines()
    print(row2)

# ellenőrzés/2:

with open("adat3.txt", "r") as f4:
    row_num = len(f4.readlines())

with open("adat3.txt", "r") as f5:
    for i in range(row_num):
        row = f5.readline()
        print(row.strip())

