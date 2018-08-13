#sum unlimited quantity of numbers


def unlimsum (**kvargs):
    sum = 0
    for key in kvargs:
        sum = sum + kvargs[key]
    return sum


b = unlimsum(b=1, c=2, a=3)


print "{}".format(b)
