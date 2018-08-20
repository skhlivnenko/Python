#print all numbers before N using functions

max = int(input("Input number"))

def output (max):
    print ("All number before are:")
    for i in range(1, max):
        print ("{}").format(i)

output(max)


#print all numbers before N using recursion

num = int(input("Input number"))

def output (num):
    if num == 1 :
        return 1
    return "{}\n{}".format(output(num-1),num)
print output(num)


################## Teacher example
n = int(input("Input number"))
def f(n):
    if n==1:
        return 1
    return "{}\n{}".format(f(n-1),n)
print f(n)

