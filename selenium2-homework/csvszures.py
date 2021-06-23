# 003 Feladat: Python CSV filekezelés

import csv

def copy():
    filename = "table_in.csv"
    with open(filename, "r", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            with open("table_new.txt", "a", encoding='utf-8') as f:
                name = row[0].strip()
                mail = row[1].strip()
                f.write(f'{mail},{name}\n')

def delet():
    with open("table_new.txt", "w") as f:
        f.write('')

delet()
copy()
