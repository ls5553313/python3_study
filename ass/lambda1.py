fx = lambda n  : True if (n**2 + 1) % 5 ==0 else False
print(fx(3))
print(fx(4))

fx = lambda x,y : x if x > y else y
print(fx(100, 200))