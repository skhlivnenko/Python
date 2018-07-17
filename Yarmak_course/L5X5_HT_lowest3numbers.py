# There is an array. Find 3 serial numbers in array, which gives biggest total

numbers = [12, 23, 34, 5, 6, 3, 434, 4]


def find_biggest(numbers):
    biggest_total = 0  # shows total of elements

    for i in range(0, len(numbers) - 2):  # look for elements in array
        current_total = numbers[i] + numbers[i + 1] + numbers[i + 2]  # compute total of next 3 numbers
        if current_total >= biggest_total:  # is this total is bigger than biggest previous
            biggest_total = current_total  # save current total as biggest total
            biggest_numbers = [numbers[i], numbers[i+1], numbers[i+2]]  # save win combination

    return biggest_numbers


print "In the array of {} \nThe biggest total of 3 elements is in sequence {}".format(numbers, find_biggest(numbers))