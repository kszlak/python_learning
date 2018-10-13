cars = ['Peugeot', 'Fiat', 'Volvo']
print (cars[0])
print (cars[1])

for x in cars:
    print x

for x in range (len(cars)):
    print ("Index: " + str(x) + " : " + cars[x] )

l = cars[2]
for x in cars[2:3]:
    print(x)

#w python string dziala z indeksem

nazwa = "Honda"
print (nazwa[:2])
