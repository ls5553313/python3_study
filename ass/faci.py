l = [1, 1]
for i in range(38):
    a = int(l[i]) + int(l[i+1])
    l.append(a)
print(l)
print(len(l))