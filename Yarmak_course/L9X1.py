class HandleList:
    def update(self, a):
        if isinstance(a, list):
            a.append(1)


class HandleDict:
    def update(self, a):
        if isinstance(self, a):
            a.update({"1": "one"})


handles = [HandleList, HandleDict]
a = []
for h in handles:
    h.update(a)

