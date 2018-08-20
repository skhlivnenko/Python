def decor(fn):
    def d1(x):
        return "'{}'".format(fn(x))
    return d1  # decorator returns only function!


@decor  # shows that function fm is decorated
def fm(a):
    return a.lower()


b = fm("Hello")
print (b)

b = decor(fm)("Hello")
print(b)

