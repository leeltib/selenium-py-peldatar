# 010 Feladat: Python lista gyakorlása

print("Készíts egy pozitív egész számokból álló listát! Kilépni 0-val tudsz.")
list_elem = int(input("Milyen számot szeretnél? "))

lista = []
while True:
    if list_elem > 0:
        lista.append(list_elem)
        list_elem = int(input("Kérem a következő számot "))
    else:
        print("Ezzel befejezted a listaépítést.")
        break

print("A létrehozott lista, fordított elem sorrenddel kiírva:")
print(lista[::-1])     # csak a kiíratást fordítom meg, a lista tartalom nem változik meg
#print(lista)

# a reverse() függvénnyel megváltozik az eredeti lista tartalma, megfordul a sorrend
lista.reverse()
#print(lista)


