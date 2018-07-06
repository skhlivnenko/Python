a=input("Input first number: ")
b=input("Input second number: ")
c=input("Input third number: ")

if a<c and a<b:
    print "First is lowest ({})".format(a)
elif b<c and b<a:
    print "Second is lowest ({})".format(b)
else:
    print "Third is lowest ({})".format(c)

