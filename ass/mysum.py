def mysum(n):
    L = [x for x in range(1,n+1)]
    return(sum(L))

def myfac(n):
    i = 1
    for x in range(1,n+1):
        i = i * x
    return(i)

def mysum1(*args):
    a = 0
    for i in args:
        a += i
    return(a)



def myrange(a , b = None, c=1):
    if b is None:
        b = a
        a = 0
    l = []
    while a < b:
        l.append(a)
        a += c
    return(l)
print(myrange(10 , 5))
L = [x for x in range(10, 5)]
print(L)





