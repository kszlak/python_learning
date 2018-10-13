baza = {"volvo": 7.8,
        "bmw": 4.0,
        "fiat": 6.5,
        "mercedes": 5.0}

marka = raw_input('Podaj marke: ')
km = raw_input('Ile km: ')
il = 100.0

if marka in baza:
    spalanie = baza[marka]*(float(km)/100)
    print("Spalil: " + str(spalanie))
