
x = int(input(":"))
a = ""
for s in range(2, x):
    if x % s == 0:
        print("no")
        break
    else:
        a = str("yes")
print(a)
