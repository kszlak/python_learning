#read from file
def get_dane():
    file = open("animals.txt", "r")
    file2 = file.read()
    file3 = file2.split("\n")
    del file3[-1]
    return file3

    #Alternative:
    #for l in file:
    #    file.append(l.strip())
    #file.close()

def main():
    lista = get_dane()
    while True:
        x = raw_input("Do you want add an animal? ")
        if x == "yes":
            y = raw_input("Add an animal: ")
            lista.append(y)
        if x =="no":
            break
    print lista

if __name__== "__main__":
    main()
