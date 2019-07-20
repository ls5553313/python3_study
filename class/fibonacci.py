from time import *

class fibonacci:
    def __init__(self, number):
      self.number = number
      self.x,self.y = 0,1
      self.i = 0
    def __repr__(self):
        l = [111,111]
        return(l)
    # def __str__(self):
    #     l = [111,111]
    #     return('l')

    def __iter__(self):
        while self.i < self.number:
            self.i += 1
            self.x,self.y = self.y,self.x+self.y
            yield self.x
    def __next__(self):
        while self.i < self.number:
            self.i += 1
            self.x,self.y = self.y,self.x+self.y
            return self.x
        else:
            raise StopIteration

class iter_fibonacci():
    def __init__(self, number):
        self.i = 0
        self.number = number
        self.x,self.y = 0,1
    def __next__(self):
        while self.i < self.number:
            self.i += 1
            self.x,self.y = self.y,self.x+self.y
            return self.x
        else:
            raise StopIteration

for x in fibonacci(30):
    print(x, end=',')
print()
print([x for x in fibonacci(30)])
print(sum(fibonacci(30)))
v = fibonacci(5)
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
