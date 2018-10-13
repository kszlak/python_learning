baza = {"volvo": 1.8,
        "bmw": 4.0,
        "fiat": 1.5,
        "mercedes": 5.0}

marka + raw_input('Podaj marke')
podaj_km = 100

if marka in baza:
    spalanie = baza[marka]
    print(S"Ile na 100: " + spalanie)
