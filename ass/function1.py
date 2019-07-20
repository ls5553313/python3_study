def isprime(a):
    a1 = bool()
    for s in range(2, a):
        if a % s == 0:
            a1 = False
            break
        else:
            a1 = True
    return(a1)
#x = int(input("pls input an int: "))
#a2 = isprime(x)
#print(a2)


def prime_m2n(m,n):
    L = []
    for x in range(m,n):
        if isprime(x):
            L.append(x)
    return(L)

#m1 = int(input("m = "))
#m2 = int(input("n = "))

#L1 = prime_m2n(m1,m2)
#print(L1)

def primes(m):
    L = []
    for x in range(m):
        if isprime(x):
            L.append(x)
    return(L)
        

m1 = int(input("m = "))
L1 = primes(m1)
print(L1)
print(sum(L1))
