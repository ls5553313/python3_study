s1 = "ABC"
s2 = "123"
l = [x+y for x in s1 for y in s2]
print(l)

l = []
while True:
    s = str(input("pls input:"))
    if not s:
        break
    l.append(s)
print(l)

l1 = []
for i1 in l:
    if i1 not in l1:
        l1.append(i1)
print(l1)

