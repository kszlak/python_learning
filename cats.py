def data_cats():
    cats = []
    while True:
        ask = raw_input("Want to add a cat? y/n\n")
        if ask == "y":
            name = raw_input("Write name: \n")
            cats.append(name)
        else: break
    return cats

def main():
    kitty = data_cats()
    i = 0
    print kitty
    for s in range(len(kitty)):
        i = i+1
        print ("Cat {0}: {1}".format(i, kitty[s]))


if __name__=="__main__":
    main()
