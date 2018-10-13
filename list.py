#Add function

def print_tab(a):
    for x in range (len(cars)):
        print ("Index: " + str(x) + " : " + cars[x])

if __name__=="__main__":
    cars = ['Peugeot', 'Fiat', 'Volvo']

print_tab(cars)
