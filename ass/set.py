s1 = set()
s2 = set()
L = []
while True:
    x = input("pls input: ")
    if not x:
        break
    s1.add(x)
    if s1 - s2:
        L.append(x)
        print(L)
    s2.add(x)
print(len(s1))

for y in L:
    print(y)

