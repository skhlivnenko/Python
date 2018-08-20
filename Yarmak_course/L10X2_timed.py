# task: to measure working time of function using decorator

import time

# DECORATOR
def decor_time(function2decor):        # give core function for decoration
    def measure_time():
        t1 = time.time()                # check start time
        result_of_function2decor = function2decor()   # call core function
        t2 = time.time()                # check finish time
        dt = t2-t1
        print"function working time is {} sec".format(dt)
        return result_of_function2decor  # return result of core function, because decorator save the same result
    return measure_time


@decor_time                             # apply decorator decor_time
def some_func():                        # core function
    for i in range(20000000):
        a = i*i
    return a


result = some_func()
print "core function result = {}".format(result)


