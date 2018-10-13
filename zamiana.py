haslo = "secret"
srodek = '*' * (len(haslo)-2)
x = haslo[0] + "XXX" + haslo[-1]
print x
