class OrderSet:
    def __init__(self, iterator):
        self.iterator = set(iterator)

    def __and__(self,rhs):
        l = self.iterator & rhs.iterator
        return OrderSet(l)
        
    def __or__(self,rhs):
        l = self.iterator | rhs.iterator
        return OrderSet(l)

    def __xor__(self,rhs):
        l = self.iterator ^ rhs.iterator
        return OrderSet(l)

    def __eq__(self,rhs):
        if self.iterator == rhs.iterator:
            return True
        else:
            return False

    def __ne__(self,rhs):
        if self.iterator != rhs.iterator:
            return True
        else:
            return False

    def __contains__(self,val):
        if val in self.iterator:
            return True
        else:
            return False

    def __repr__(self):
        return "OrderSet(%s)" % str(list(self.iterator))

s1 = OrderSet([1,2,3,4])
s2 = OrderSet([3,4,5])
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
a1 = (OrderSet([1,2,3]) != OrderSet([1,2,3,4]))
a2 = (s2 == OrderSet([1,2,3,4]))
a3 = (2 in s2)
print(a1)
print(a2)
print(a3)