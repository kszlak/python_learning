plik = open("File")

haslo=raw_input("Podaj haslo: ")
srodek = '*' * (len(haslo)-2)
x = haslo[0] + srodek + haslo[-1]
print x
plik.write(x)
