#find a sum of digits of inputed natural number using FOR

number = str(input("Input random natural number\n")) #input and convert to string
sum = 0
length = len(number) #count elements in String. Attribute len didn't work with Py.3+

for i in range(0,length):
    sum = sum + int(number[i])

print ("The sum of digits using for is {}").format(sum)



"""
find a sum of digits of inputed natural number using using WHILE
"""

sum2 = 0
v = 0
while v < length:
    sum2 = sum2 + int(number[v])
    v = v + 1

print ("The sum of digits using while is {}").format(sum2)
