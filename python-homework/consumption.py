# Autó fogyasztás számolás

fogy_ou = float(input("Az autód országúti fogyasztása (liter/100 km): "))
fogy_va = float(input("Az autód városi fogyasztása (liter/100 km): "))

km_ou = float(input("Országúton megtett kilóméterek száma: "))
km_va = float(input("Városban megtett kilóméterek száma: "))

uzany_ar = int(input("Egy liter üzemanyag ára: "))

fogy_szakasz = ((km_ou * fogy_ou) / 100) + ((km_va * fogy_va) / 100)

print(f"Odafelé várhatóan {round(fogy_szakasz, 1)} liter lesz az üzemanyag fogyasztásod.")
print(f"Így összesen {round(fogy_szakasz*2, 1)} litert használsz majd el oda-vissza.")
print(f"A teljes út üzemanyag költsége {int((fogy_szakasz*2) * uzany_ar)} Ft lesz.")

