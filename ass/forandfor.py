i = int(input("pls input: "))
for s1 in range(i):
    for s2 in range(1, i + 1):
        print(s2, end = " ")
    print()

s1 = 0
s2 = 0
i = int(input("pls input: "))
for s1 in range(i):
    s2 += 1
    for s3 in range(s2, i + s2):
        print(s3 , end = " ")
    print()
 