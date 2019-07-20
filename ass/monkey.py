def monkey(a,b):
    for i in range(1,b):
        a = (1 + a) * 2
    return(a)
#print(monkey(1,3))

def totalnumber(x):
    L = []
    for i in range(1,x):
        if x % i == 0:
            L.append(i)
    if sum(L) == x:
        return(x)
def main(n):
    L = []
    for i in range(n):
        if totalnumber(i):
            L.append(totalnumber(i))
    return(L)

print(main(10000))

    
    

