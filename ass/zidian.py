d = {}
while True:
    s = str(input("string:"))
    if not s:
        break
    i = 1
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1 
    print(d)
for i1,i2 in d.items():
    print(i1, ":", i2)
