class mylist(list):
    def insert_heat(self,value):
        self.insert(0,value)


l = mylist(range(5))
l.insert_heat(-1)
print(l)
