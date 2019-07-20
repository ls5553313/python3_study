# ass.py

import re

file  = open('1.txt')

dic = []
i = 0
l11 = ''
l22 = ''
for l in file:
    if re.findall("is .*, line protocol is .*", l):
    # if re.findall("^\w+", l):
        l1 = re.split(" +", l)
        l11 = l1[0]
        # print(l11)
    
    if re.findall("  Internet address is ", l):
        l2 = re.split("  Internet address is ", l)
        l22 = l2[1].rstrip()
        # print(l22)
    if l == '\n':
        dic.append((l11,l22))
        l11 = ''
        l22 = ''
        i += 1
# print(i)
for i in dic:
    print(i)

file.close()

# file  = open('1.txt')
# partern = ""
# i = 0
# for l in file:
#     if l == '\n':
#         i += 1
# print(i)
