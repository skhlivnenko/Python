"""""""""
We can predefine b in f(a,b) using f(a,b=3)
Operator "pass" do nothing
Function always returns None in case "return" is absent
It could be written as f(b=1, a=3, c =7)

Task: Write function of sum 3 numbers tranfering arguments not different orders
"""""

a = int(input("Input A"))
b = int(input("Input B"))
c = int(input("Input C"))

def sum (a,b,c):
    result = a + b + c
    return result

print sum (b=a,a=b,c=c)