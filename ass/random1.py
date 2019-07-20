import ceshi
x = random.random()
i = 0
while True:
    y = int(input('pls input a number: '))
    i += 1
    if y == x:
        print("correct")
        print("use" + i + "times")
        break
    elif y > x:
        print("bigger than x")
        print("use" + i + "times")
    else:
        print("smaller than x")
        print("use" + i + "times")
print("use" + i + "times")