#add value to unknown object dictionary or list

a = {}  # dictionary
# a = []  # list


def add_element():
    if isinstance(a, dict):
        a.update({1: "one"})
        print "dict updated"

    if isinstance(a, type({})):
        a.update({1: "one"})
        print "dict updated"

    if isinstance(a, list):
        a.append(1)
        a.append("one")
        print "list updated"


add_element()
print a
