import random

s1= list('/*-+')
s2 = 'A23456789JQK'
print(s1)
L = [x + y for x in s1 for y in s2 ]
L += [x + '10' for x in s1]
L += ['king','queen']
print(L)
fapai(L)
def fapai(l):
    l1 = random.sample(l,17)
    for x in l1:
        l.remove(x)
    l2 = random.sample(l,17)
    for y in l1:
        l.remove(y)
    l3 = random.sample(l,17)
    for z in l1:
        l.remove(z)
    print(l1,l2,l3,l)


