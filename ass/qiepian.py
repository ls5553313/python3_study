L = [3, 5]
L[1:1] = [4]
L[:0] = [1,2]
L[-1:-1] = [6] 
print(L)

i1 = 0
a = list(range(6))
print(a)
while i1 < 6:
    a[(5 - i1)] = L[i1]
    i1 += 1
del a[len(a) - 1]
print(a) 
