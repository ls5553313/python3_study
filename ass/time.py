import time
print(time.localtime())

#while True:
#    time.sleep(1)
#    print(time.strftime('%H:%M:%S',time.localtime()))

Hour = int(input("pls input h: "))
Minute = int(input("pls input m: "))
Second = int(input("pls input second: "))
while True:
    time.sleep(1)
    t = time.localtime()
    print(t[3],t[4],t[5])
    if t[3] == Hour and t[4] == Minute and t[5] == Second:
        print("time **************")
    #if t[3] == 