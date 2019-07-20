def high(n):
    h = 100 * 0.5**n
    return(h)
def distance(n):
    x = sum(map(lambda i: high(i -1) + high(i),range(1,n+1)))
    return(x)
print(high(10))
print(distance(10))
          
def is_prime(i):
    if i <= 1:
        return False
    for x in range(2,i):
        if i % x == 0:
            return False
    return True

def zhiyinshu(i):
    l = []
    for x in range(2,i+1):
        if is_prime(x) and i % x ==0:
            l = l + [x] + zhiyinshu(int(i / x))
            break
    return(l)
        

print(is_prime(2))
print(zhiyinshu(120))
            
            


