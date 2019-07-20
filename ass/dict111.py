d = {}
while True:
    s1 = str(input("pls input name:"))
    if not s1:
        break
    s2 = str(input("pls input explanation:"))
    d[s1] = s2
    print(d)
s = str(input("pls input name:"))
if s in d :
    print(d[s])
else:
    print(s, "is not in d")