# 017 Feladat: Python dictionary gyakorlása

text_f1 = ""
with open('text_017.txt', 'r', encoding='utf-8') as file:
    for sor in file:
        sor1 = sor.replace(",", "").replace("-", "").replace("_", "").replace(":", "").replace(".", "").replace("!", "").replace("?", "").replace(";", "").replace('"', "").replace("=", "").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")
        sor2 = sor1.strip().lower()
#        print(sor2)
        text_f1 += str(sor2 + " ")    # a letisztított, kisbetűsített sorokat kiírjuk egyetlen string változőba (text_f1)

text_f2 = text_f1.split()       # az összes szó egy listába íródik, az ismétlődések is újabb és újabb listaelemek
#print(text_f2)
#print(type(text_f2))

text_f3 = set(text_f2)          # list-set-list konvertálás után a text_f4 már csak egyszer tartalmaz minden szót
text_f4 = list(text_f3)
text_f4.sort()                  # a szavak sorba rendezése
#print(text_f4)

dict = {}
for i in text_f4:               # végigmegyünk a szavakon (text_f4 lista elemei)
    num = text_f2.count(i)      # megszámoljuk az egyes szavak előfordulását (text_f2 lista alapján)
    dict[i] = num               # az aktuális szó - előfordulás párost hozzáadjuk új elemként a dict dictionary-hez
#print(dict)

print("-" * 90)
print("A text_017.txt fájlban levő szövegben előforduló szavak, és azok előfordulási gyakorisága:")
print("-" * 90)
row = 0
for key, value in dict.items():
    row += 1
    print(f'{row}. szó: "{key}", előfordulások száma: {value}')


