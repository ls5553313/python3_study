l1= [str(input("input:"))]

print(l1)
while True:
    l2 = [str(input("input:"))]
    if l2 == ["1"]:
        break
    l1 += l2
    print(l1)

l1.reverse()

i = 0
j = 0
while i < len(l1):
    s = l1[i]
    j += len(s)
    print(l1[i])
    i += 1
print(j)



