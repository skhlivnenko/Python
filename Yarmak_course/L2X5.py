#UP TO 3x3

#using "for"
for v in range(1,10):
    print "{}".format(v*3)
    if v>2: break

#using "while"
w = 3
while w<= 3*9:
    print "{}".format(w)
    w +=3 #increment 3, equal w=w+3
    if w > 3*3: break

#SKIP 3 and 4

#using "for"
for v in range(1,10):
    if v == 3 or v == 4: continue
    print "{}".format(v*3)


#using "while"
w = 3
while w<= 3*9:

    if w == 3*3 or w == 3*4:
        w += 3  # increment 3, equal w=w+3
        continue

    print "{}".format(w)
    w += 3  # increment 3, equal w=w+3


