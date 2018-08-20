# tranform library to list

libr = {0, "zero", 1, "first", 2, "second"}
arr = []

# for k,v in libr.items():
#    arr.append(k,v)

for pair in libr:
    arr.append(pair)

print "{}".format(arr)