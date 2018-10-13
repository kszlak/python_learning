#Hides the middle of the password with def

def hide_passwd(a):
    middle = '*' * (len(passw)-2)
    x = passw[0] + middle + passw[-1]
    print x

if __name__=="__main__":
    passw=raw_input("Input password: ")

hide_passwd(passw)
