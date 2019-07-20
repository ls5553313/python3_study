# fork_zombie.py

import os
import time 

pid = os.fork()

if pid < 0:
    print("failed to create process")
elif pid == 0:
    print("Child process: ", os.getpid())
    print("Child process exit")
else:
    print("parent process")
    while True:
        pass