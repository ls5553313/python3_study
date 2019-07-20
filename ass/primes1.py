from fenjieyinshu import isprime 

def primes(m,n):
    while m < n:
        if isprime(m):
            yield m
        m += 1

L = [x for x in primes(10,30)]
print(L)