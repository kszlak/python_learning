tab=[]
q=0

while True:
    x = raw_input ("Do you want to add a cat? ")
    if x == "yes":
        y = raw_input ("Add a cat: ")
        print y
        tab.append(y)
    elif x=="no":
        for s in range (len(tab)):
            print ("Kitty {0}: {1}".format(s, tab[s]))
        break
