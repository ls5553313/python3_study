import os
import re


file = open('1.txt')
while True:
    data = file.read(1024)
    reg = re.findall(r"[A-Z][a-z]*\b",data)
    print(reg)
    if len(data) < 1024:
        break
file.close()


file = open('test.txt')
while True:
    data = file.read(4096)
    pat = r"-?\d+(\.?\d*)?/?%?(\d+(\.?\d*)?)?"
    reg = re.finditer(pat,data)
    for i in reg:
        print(i.group())
    print("======")
    if len(data) < 1024:
        break
file.close()