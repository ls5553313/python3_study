# muiltiprocessing.py

from multiprocessing import Process
import os

#file = open("dd.txt","r")

def save1():
    file = open("dd.txt","r")
    a = file.readlines()
    s = "".join(a)
    print(len(s))
    half = len(s)//2
    print(half)
    file.close()

    file = open("dd.txt","r")
    a = file.read(half)
    print(a)
    file.close()

    file1 = open("dd1.txt","w")
    file1.write(a)
    file1.close()

def save2():
    file = open("dd.txt","r")
    a = file.readlines()
    s = "".join(a)
    print(len(s))
    half = len(s)//2
    print(half)
    file.close()

    file = open("dd.txt","r")
    a = file.read(half)
    a = file.read()
    print(a)
    file.close()
    
    file1 = open("dd2.txt","w")
    file1.write(a)
    file1.close()

p1 = Process(target = save1)
p2 = Process(target = save2)

p1.start()
p2.start()

p1.join()
p2.join()



