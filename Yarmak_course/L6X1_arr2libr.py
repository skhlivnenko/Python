# get library from array, using index as key

arr = ["zero", "first", "second"]

libr = {}                       # create new library
for i in range(len(arr)):       # Note: use len(arr) instead of (0,len(arr))
                                # for index "i" create key "i" and save array value
    libr[i] = arr[i]            # 1 variant
#   libr.update({i:arr[i]})     # 2 variant

print"{}".format(libr)