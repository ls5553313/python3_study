i = int(input("int: "))
j = 2 * i - 1
x = 1
while x <= i:
    s1 = (2 * x - 1)* "*"
    s1 = s1.center(j)
    print(s1)
    x += 1
x = 1
while x <= i:
    s1 = "*"
    s1 = s1.center(j)
    print(s1)
    x += 1