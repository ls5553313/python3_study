l = []
l1 = 0
l2 = 0
l3 = 0
while True:
    d = {}
    s1 = str(input("name: "))
    if not s1:
        break
    d['name'] = s1
    d['age'] = int(input("age: "))
    d['score'] = int(input("score: "))
    print(d)
    l.append(d)
    if len(str(d['name'])) > l1:
        l1 = len(str(d['name']))
    if len(str(d['age'])) > l2:
        l2 = len(str(d['age']))
    if len(str(d['score'])) > l3:
        l3 = len(str(d['score']))

print(l)
line1 = ("+" + (l1 + 2)*'-' + "+" +
         (l2 + 2)*'-' + "+" +
         (l3 + 2)*'-' + "+")
ss1 = 'name'
ss3 = 'score'
ss2 = 'age' 
line2 = ("|" + ss1.center(l1 + 2) + "|" +
         ss2.center(l2 + 2) + "|" +
         ss3.center(l3 + 2) + "|")
print(line1)
print(line2)
print(line1)
for x in range(len(l)):
    line3 = ("|" + str(l[x][ss1]).center(l1 + 2) + "|" +
         str(l[x][ss2]).center(l2 + 2) + "|" +
         str(l[x][ss3]).center(l3 + 2) + "|")
    print(line3)
print(line1)

