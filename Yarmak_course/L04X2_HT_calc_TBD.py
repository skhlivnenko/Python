#write a calculator with console input, that works with +,-,*,/


expression = raw_input("Input expression")
#check input: print "{}".format(expression)

operators = ["+","-","*","/"]

#parse first number until meet operator
i=0
element1 = ""


for i in range(0,len(expression)):
    for v in range(0, len(operators)):
        if expression[i] == operators[v]: break
        break
    element1 += expression[i]


print element1



#parse operator
#parse next number
#describe functions for every operator
#start calculation
#print result


