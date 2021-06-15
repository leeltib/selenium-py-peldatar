
kor = int(input("Hány éves? "))
ital = input("Mit kér? Sört vagy kólát tudok adni. ")

if kor < 18 and ital == "sört":
    print("Sajnálom, de neked nem adhatok alkoholt.")
elif kor > 60 and ital == "kólát":
    print("Tudja, hogy a koffein megemelheti a vérnyomását?")
elif kor >= 18 and ital == "sört":
    print("Parancsoljon a söre!")
elif kor <= 60 and ital == "kólát":
    print("Parancsoljon a kólája!")
else:
    print("Csak sört vagy kólát tudok adni!")
