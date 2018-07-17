# There is an array. Find 3 serial numbers in array, which gives biggest total

numbers = [12, 23, 34, 5, 6, 3, 434, 4]


def find_biggest (numbers):
    biggest_total = 0  # shows total of elements

    for i in range(0, len(numbers) - 2):  # look for elements in array
        if numbers[i] + numbers[i + 1] + numbers[i + 2] >= biggest_total:  # is next 3 element i bigger than previous
            biggest_total = numbers[i] + numbers[i + 1] + numbers[i + 2]  # save biggest total to compare next
            biggest_numbers = [numbers[i], numbers[i+1], numbers[i+2]]  # save win combination

    return biggest_numbers


print "In the array of {} \nThe biggest total of 3 elements is in sequence {}".format(numbers, find_biggest(numbers))