numbers = (1,2,3,0,45,6,7)

#odd 1,3... #even 2,4...

def even_odd (numbers):
    odd_qty = 0
    even_qty = 0
    null_qty = 0

    for item in numbers:
        if item % 2 == 1:
            odd_qty += 1
        elif item == 0:
            null_qty += 1
        else:
            even_qty += 1

    print "In this list {} are {} odd and {} even numbers".format(numbers, odd_qty, even_qty)

even_odd(numbers)