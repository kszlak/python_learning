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
                last_character = s[-1]
                print (last_character)

for z in tab:
    print z
