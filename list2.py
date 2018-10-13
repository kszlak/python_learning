base = {"volvo": 7.8,
        "bmw": 4.0,
        "fiat": 6.5,
        "mercedes": 5.0}

brand = raw_input('Input brand: ')
km = raw_input('How many km: ')
q = 100.0

if brand in base:
    combustion = base[brand]*(float(km)/100)
    print("Sum of combustion: " + str(combustion))
