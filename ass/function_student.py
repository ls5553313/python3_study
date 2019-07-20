def input_student():
    l = []
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
    return(l)

def vary(L):
    l1 = 4
    l2 = 3
    l3 = 5
    for x in L:
        if len(str(x['name'])) > l1:
            l1 = len(str(x['name']))
        if len(str(x['age'])) > l2:
            l2 = len(str(x['age']))
        if len(str(x['score'])) > l3:
            l3 = len(str(x['score']))
    return(l1,l2,l3)

def output_student(l):
    l1,l2,l3 = vary(l)
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


def change(l):
    s = str(input("pls input student name: "))
    result = not True
    for x in l:
        while x['name'] == s:
            result = True
            x["name"] = str(input("pls input new name:"))
            x["age"] = int(input("pls input new age:"))
            x["score"] = str(input("pls input new score:"))
            print(x)
            print("正确按１，不正确按２")
            i = int(input("pls input 1 or 2"))
            if s == 1:
                break
    if not result:
        print ('cant find')




def delete(l):
    s = str(input("pls input student name: "))
    i = 0
    result = not True
    for x in l:
        while x['name'] == s:
            result = True
            print(x)
            print("确认删除吗？确认按１，不按２")
            i1 = int(input("pls input 1 or 2: "))
            if i1 == 1:
                del l[i]
                print(l)
                break
            else:
                break
        i += 1
    if not result:
        print ('cant find')

def output_accord_score_reversefalse(l):
    def get_score(d):
        return(d['score'])
    sorted(l, key = lambda x : x['score'])
    return(l)


L = [{'score': 1, 'age': 1, 'name': '1'}, 
    {'score': 2, 'age': 2, 'name': '2'}, 
    {'score': 33, 'age': 33, 'name': '33'}]
print(output_accord_score_reversefalse(L))


def main():
    L = []
    while True:
        print(("1 = zenjia, \n2 = shuchu, \n3 = genggai, \n4 = shanchu, \nq = quit"))
        i = str(input("pls input 1 2 3 4 q : "))
        if i =='1':
            L += input_student()
        elif i =='2':
            output_student(L)
        elif i =='3':
            change(L)
        elif i =='4':
            delete(L)
        elif i =='q':
            break

    





