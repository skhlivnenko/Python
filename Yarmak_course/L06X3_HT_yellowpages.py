def main():
    catalog = {}
    catalog.update({"John","380937452343"})
    return catalog


def menu ():
    print "Yellow pages: \n1. Find contact \n2. Add contact\n3. Delete contact \n4. Exit"
    mode = input("Enter a menu item number: ")
    print "You entered {}".format(mode)

def add_contact():
    catalog = {}
    name = raw_input ("Enter a name: ")
    phone_number = raw_input("Enter a phone number: ")
    catalog.update({name: phone_number})
    print catalog
    print "{}".format(name)

#main()

#menu()

add_contact()
