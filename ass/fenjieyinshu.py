def isprime(n):
    if n <= 1:
        return False
    else:
        for x in range(2,n):
            if n % x ==0:
                return False
        else:
            return True

def get_prime_list(n):
    l = []
    while not isprime(n):
        for x in range(2,n):
            if isprime(x) and n % x == 0:
                l.append(x)
                n = int(n / x)
                print(l,n)
                break
    else:
        l.append(n)
    return(l)
print(get_prime_list(90))

