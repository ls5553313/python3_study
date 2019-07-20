i = int(input("pls input: "))
j = 1
while j <= i:
    s = str((i - j) * " " + j * "*")
    print(s)
    j += 1
j = 1
while j <= i:
    s = str( (j - 1)* " " + (i - j + 1) * "*")
    print(s)
    j += 1
j = 1
while j <= i:
    s = str((i - j + 1) * "*" + (j - 1)* " ")
    print(s)
    j += 1

j = 1
while j <= i:
    #s = %s % j * "*"
    s1 = str("%" + str(i) + "s")
    print(s1 % (j * "*"))
    j += 1
j = 1
while j <= i:
    #s = %s % (i - j + 1) * "*" 
    s1 = str("%" + str(i) + "s")
    print(s1 % ((i - j + 1) * "*"))
    j += 1
j = 1
while j <= i:
    #s = %-s % (i - j + 1) * "*" 
    s1 = str("%" + "-" + str(i) + "s")
    print(s1 % ((i - j + 1) * "*"))
    j += 1