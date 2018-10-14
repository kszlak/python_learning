def get_dane():
    return [
        {'nazwa':'mleko', 'cena':4.5},
        {'nazwa':'maslo', 'cena':4.5},
        {'nazwa':'czekolada', 'cena':8.5},
        {'nazwa':'ryz', 'cena':6},
    ]


def main():
    basket = get_dane()
    suma=0

    file = open("storage.csv","w")

    for s in basket:
        suma=suma+s['cena']
        print(s['nazwa'] + ','+ str(s['cena']))
        wynik = (s['nazwa'] + ','+ str(s['cena']) + '\n')
        file.write(wynik)
    file.close()

if __name__== "__main__":
    main()
