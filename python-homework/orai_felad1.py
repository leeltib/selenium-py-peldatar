# Egy autokereskedes honlapjan vagyunk. Krealjunk egy menut, az alabbi menupontokkal:
# 1, Kocsi felvetel.  Itt be kell tudni adni az auto markajat es, hogy mennyi idos a kocsi.
# 2, Osszes kocsi adatai lekerdezese
# 3, Kocsi adatainak lekerdezese index alapjan. (marka, eletkora)
# 4, Kocsi eladasa
# 5, Kilepes az applicaciobol

def print_menu():
    menuk = ["1. Felvétel", "2. Adatlekérés-összes", "3. Adatlekérés-egyéni", "4. Eladás", "5. Kilépés"]
    for menu in menuk:
        print(menu)
    # itt kódold a menü kiiratást

def ask_user_input_for_menu():
    menu_opc = ["1", "2", "3", "4", "5"]
    menu_num = input("Válassz menüt! ")
    if menu_num in menu_opc:
        return menu_num
    else:
        return '9'
    # itt kodold le az adatbekérést

def register_car(m, k):
    car = []
    car.append(m)
    car.append(k)
    cars.append(car)
    # itt kodold le az auto regisztraciojat / adatbekereset / menteset a memoriaban valamilyen kontener tipusu valtozo
    # vagy valtozokba, miert ne lehetne tobb is az egyszeruseg kedveert

def cars_details(list):
    num = 0
    for i in list:
        num += 1
        print(f"Check-{num}: típus: {i[0]}, kor: {i[1]}")
    # ide kodold le a memoriaban levo osszes kocsi kinyomtatasat a konzolra

def car_details_by_id(car_index):
    car_num = car_index - 1
    print(f"{car_index}. típus: {cars[car_num][0]}, kor: {cars[car_num][1]}")
    # ide kodold le annak az egy darab kocsi adatainak kiiratasat ami az adott car_index index alatt van tarolva a
    # valtozo(k)-ban

def car_sell(car_index):
    car_num = car_index - 1
    cars.remove(cars[car_num])
    # ide kodol le az auto eladasat / torleset a memoriaban levo tarolobol

def start_application():
    # a menukezelest megirtam neked
    print("Welcome to PM car dealership!")
    print_menu()
    running = True
    while running:
        user_pick = int(ask_user_input_for_menu())
        if user_pick == 1:
            marka = input("Márka? ")
            kor = int(input("Hány éves? "))
            register_car(marka, kor)
        elif user_pick == 2:
            cars_details(cars)
        elif user_pick == 3:
            cars_len = len(cars)
            print(f"{cars_len} autó van a listán.")
            car_index = int(input("Hányadik adatait szeretnéd?: "))
            car_details_by_id(car_index)
        elif user_pick == 4:
            cars_len = len(cars)
            print(f"{cars_len} autó van a listán.")
            car_index = int(input("Hányadikat szeretnéd törölni?: "))
            car_sell(car_index)
        elif user_pick == 5:
            running = False
            print("Thank you. Have a nice day.")
        else:
            running = False
            print("Nincs ilyen menüpont.")

# esetlegesen ide vegyel fel global valtozot(kat) amibe(kben) tarolod az auto adatait

cars = [["Audi", 4], ["Mercedes", 6], ["Skoda", 3]]
start_application()


