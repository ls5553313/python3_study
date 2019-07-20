l = []
while True:
    s = str(input("string:"))
    if not s:
        break
    l.append(s)
    print(l)
d = {x:len(x) for x in l}
print(d)