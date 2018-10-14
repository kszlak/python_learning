#read from file
file = open("animals.txt", "r")
file2 = file.read()
file3 = file2.split("\n")
del file3[-1]
print file3


while True:
    x = raw_input("Do you want add an animal? ")
    if x == "yes":
        y = raw_input("Add an animal: ")
        file3.append(y)
    if x =="no":
        break
print file3
print file2
