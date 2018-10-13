#print last character and print all names

tab =[]
tab2=[]

while True:
    x = raw_input ("Give a name: ")

    if x=="no":
        break

    else:
        tab.append(x)
        for s in tab:
            if len(s)>0:
                ostatnia_litera = s[-1]
                print (ostatnia_litera)

for z in tab:
    print z
