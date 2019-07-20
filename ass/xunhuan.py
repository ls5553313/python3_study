L = []
while 1:
    i = int(input('int:'))
    L1 = [i]
    L = L + L1
    print(L)
    if i == -1:
        print(len(L))
        print(max(L))
        print(min(L))
        print(sum(L) / len(L))
        break
