def get_dane():
    return [
            {'nazwa':'cukier','id':1, 'kg':10, 'ilosc':2, 'cena':3.10},
            {'nazwa':'maka','id':2, 'kg':10, 'ilosc':2, 'cena':3.10},
            {'nazwa':'maslo','id':3, 'kg':20, 'ilosc':4, 'cena':3.10, 'toxic':True},
            {'nazwa':'kasza','id':4, 'kg':10, 'ilosc':2, 'cena':5.10, 'toxic':False},
            {'nazwa':'mleko','id':5, 'kg':10, 'ilosc':2, 'cena':3.10, 'toxic':True},
            ]

def main():
    ilosc_storage=0
    waga_storage=0
    cena_storage=0
    ilosc_tok=0
    ilosc_nietok=0
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


    for poz in storage:
        if "toxic" in poz:
            if poz['toxic']==True:
                ilosc_tok = ilosc_tok+1
    print("Ilosc toksycznych: " + str(ilosc_tok) + " Nazwa: " + poz['nazwa'])

    for poz2 in storage:
        if "toxic" in poz2:
            if poz2['toxic']==False:
                ilosc_nietok = ilosc_nietok+1
            else:
                ilosc_nietok = ilosc_nietok+1
    print("Ilosc nietoksycznych: " + str(ilosc_nietok) + " Nazwa: " + poz['nazwa'])

if __name__ == "__main__":
    main()
