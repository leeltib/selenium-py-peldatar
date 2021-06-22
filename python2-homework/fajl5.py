# 026 Feladat: filekezelés gyakorlása / 5

def masol():
    with open("adat.txt", "r") as f:
        row_num = len(f.readlines())
    with open("adat.txt", "r") as f2:
        for i in range(row_num):
            row = f2.readline()
            with open("adat4.txt", "a") as f3:
                f3.write(row)

def torol():
    with open("adat4.txt", "w") as f4:
        f4.write('')

torol()
masol()


