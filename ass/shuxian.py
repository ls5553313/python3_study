for i in range(100, 901):
    x = 0
    j = i
    while j:
        x += (j % 10)**3
        #print(i % 10)
        j = j//10
    if x == i:
        print (x)

d = [(x * 100 + y * 10 + z) 
     for x in range(10) 
     for y in range(10) 
     for z in range(10) 
     if (x**3 + y**3 + z**3) == (x * 100 + y * 10 + z)]
print(d)

