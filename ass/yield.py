def myinteger(n):
    i = 0
    for i in range(0,n):
        yield i

for x in myinteger(3):
    print(x)
it = myinteger(2)
print(next(it))
print(next(it))
print(next(it))

