#aktywnosc = 'jazda na rolkach'
#marka = 'powerblade'


#ilosc_treningow_pazdziernik = input('Podaj liczbe treningow:')
#i = str(ilosc_treningow_pazdziernik)

#print ('W tym miesiacu '+aktywnosc +' ' +str(i))

#czas1 = 40


#laczny_czas = (int(i)+czas1+czas2+czas3+czas4)
#print(laczny_czas)



sprzet = ['rowery', 'rolki']
ilosc = [3,4]

print(len(ilosc))

#for idx in range(len(ilosc)) :
#    print(s)

#Tablice
#sprzet = ['rowery', 'rolki']
#ilosc = [3,4]



#print("Dlugosc: {0}".format(len(sprzet)))

#for idx in range(len(sprzet)):
    #print("idx: "+ str(idx) + ": "+ sprzet[idx])
    #print(sprzet[idx] + " ilosc "+str(ilosc[idx]))

def print_dict(d):
    for key, value in d.iteritems():
        print("{0}:{1}".format(key, value))

if __name__=="__main__":
    sprzet = {'name': 'rolki', 'firma': 'powerslide', 'type': 'casual'}
print_dict(sprzet)
print_dict(sprzet)

#new
