import math

def sn(a):
    i = [1]
    i += map(lambda x: 1/math.factorial(x), range(1,a+1))
    return(i)
print(sum(sn(100)))


