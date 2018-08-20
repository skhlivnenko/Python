#sum unlimited quantity of numbers


def unlimsum (a, *args):
    sum = a
    for v in args:
        sum = sum + v
    return sum


b = unlimsum(1, 2, 3, 4, 5)


print "{}".format(b)

