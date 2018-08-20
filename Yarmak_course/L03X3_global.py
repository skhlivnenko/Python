# we have global var = 10 and it's needed to change to 7 in function

a = 10

def change():
    global a
    a = 7

change()

print "{}".format(a)
