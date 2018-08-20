class Figure(object):

    count = 0

    def __init__(self):
        Figure.count += 1
        self.color = 'red'

    def __del__(self):
        Figure.count -= 1
        print "object destroyed"


class N (Figure):
    def __init__(self):
        super(N, self).__init__()  # calls parent class init, otherwise 'color' woudn't be applied


f = Figure()
print f.color
f.__init__()
del f



