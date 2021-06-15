# Szökőév-nem szökőév megállapító függvény

def szokoev(ev):
    if ev % 400 == 0:
        print(f"{ev}: szökőév")
        return True
    elif ev % 100 == 0:
        print(f"{ev}: nem szökőév")
        return False
    elif ev % 4 == 0:
        print(f"{ev}: szökőév")
        return True
    else:
        print(f"{ev}: nem szökőév")
        return False

print("Szeretnéd tudni, hogy egy bizonyos év szökőév-e?")
evszam = int(input("Írd ide az évszámot: "))

szokoev(evszam)
