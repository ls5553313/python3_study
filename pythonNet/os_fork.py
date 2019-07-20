# os_fork.py

import os
a = 1

print("*******************")
pid = os.fork()
if pid <0:
    print(pid,"faile")
elif pid == 0:
    print(pid,"new process")
    print(a)
else:
    print(pid,"old process")

print("over")