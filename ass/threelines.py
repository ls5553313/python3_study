a = str(input("pls input 1st"))
b = str(input("pls input 2st"))
c = str(input("pls input 3st"))
l1 = len(a)
l2 = len(b)
l3 = len(c)
if l1 > l2:
    m = l1
elif l3 > l1:
    m = l3
else:
    m = l2
m = m + 2
1st = str("+" + m * "-" + "+")
2st = str("|" + (m - l1) % 2 * " " + a + (m - 
    (m - l1) % 2 - l1) * " "  + "|")
3st　= str("|" + (m - l2) % 2 * " " + b + (m - 
    (m - l2) % 2 - l2) * " "  + "|")
4st = str("|" + (m - l3) % 2 * " " + c + (m - 
    (m - l3) % 2 - l3) * " "  + "|")

print(1st)
print(2st)
print(3st)
print(4st)
print(1st)