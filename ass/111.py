a = str(input("pls input 111: "))
b = str(input("pls input 211: "))
c = str(input("pls input 311: "))
l1 = len(a)
l2 = len(b)
l3 = len(c)
m = l1
if l2 > m:
    m = l2
elif l3 > m:
    m = l3
print(m)
m = m + 2
st1 = str("+" + m * "-" + "+")
st2 = str("|" + (m - l1) // 2 * " " + a + (m - 
    (m - l1) // 2 - l1) * " "  + "|")
st3 = str("|" + ((m - l2) // 2) * " " + b + (m - 
    (m - l2) // 2 - l2) * " "  + "|")
st4 = str("|" + (m - l3) // 2 * " " + c + (m - 
    (m - l3) // 2 - l3) * " "  + "|")
print(st1)
print(st2)
print(st3)
print(st4)
print(st1)