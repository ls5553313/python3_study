class mylist:
    def __init__(self,iterable):
        self.iterable = iterable
    def __add__(self, rhs):
        l = self.iterable + rhs.iterable
        print(l)
        return mylist(l)
    def __repr__(self):
        return "mylist(%s)" % str(self.iterable)

    def __mul__(self, rhs):
        l = self.iterable * 2
        return(mylist(l))


l1 = mylist([1,2,3])
l2 = mylist([4,5,6])
l3 = l1 + l2
print(l3)
l4 = l2 + l1
print(l4)
l5 = l1 * 2
print(l5)