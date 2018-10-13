def wyswietl(d):
    for s in trening:
        print("{0}:{1}".format(s, d[s]))

if __name__=="__main__":
    trening = {"cwiczenie": "bieganie",
                "czas": 60,
                "ilosc": 4,
                "miejsce": "fitnessacademy"}
    wyswietl(trening)
