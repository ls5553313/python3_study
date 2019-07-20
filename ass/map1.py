def fx(x):
    return x ** 2
def fx1(x):
    return x ** 3
def fx3(x, y):
    return x ** y
print(sum(map(fx,range(1,10))))
print(sum(map(fx1,range(1,10))))
print(sum(map(fx3,range(1,10), range(9,0,-1))))

