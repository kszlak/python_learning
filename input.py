tab =[]

while True:
    x = raw_input ("Podaj nazwe: ")
    print x
    tab.append(x)
    for s in tab:
        if len(s)>0:
            ostatnia_litera = s[-1]
            print (ostatnia_litera)
