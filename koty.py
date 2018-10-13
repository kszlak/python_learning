tablica=[]
il=0



while True:
    x = raw_input ("Czy chesz dodac kotka: ")
        if x=="tak":
            y = raw_input ("Podaj kotka: ")
            print y
            tablica.append(y)
            il=il+1
        elif x=="nie":
            for s in tablica:
                print ("Mamy " + tablica[s])
