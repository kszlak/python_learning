
def get_dane():
    return [
            {'nazwa':'cukier','id':1, 'kg':10, 'ilosc':2, 'cena':3.10},
            {'nazwa':'maka','id':2, 'kg':10, 'ilosc':2, 'cena':3.10},
            {'nazwa':'maslo','id':3, 'kg':20, 'ilosc':4, 'cena':3.10},
            {'nazwa':'kasza','id':4, 'kg':10, 'ilosc':2, 'cena':5.10},
            {'nazwa':'mleko','id':5, 'kg':10, 'ilosc':2, 'cena':3.10},
            ]

def main():
    ilosc_storage=0
    waga_storage=0
    cena_storage=0
    wybory=['kasza','maslo']

    storage =get_dane()

    for s in storage:
        if s['nazwa'] in wybory:
            ilosc_storage = ilosc_storage + s['ilosc']
            waga_storage = waga_storage + s['kg']
            cena_storage = cena_storage + s['cena']
    print ('ilosc: '+ str(ilosc_storage))
    print ('waga: '+ str(waga_storage))
    print ('cena: '+ str(cena_storage))

if __name__ == "__main__":
    main()
