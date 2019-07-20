# driver.py

from signal import * 
import time
from multiprocessing import Process,Value
import os

driver_pid = Value('i', 0)
seller_pid = Value('i', 0)

def driver_handler(sig,frame):
    
    if sig == SIGUSR1:
        print("Bus start")
    elif sig == SIGUSR2:
        print("speed over limit")
    elif sig == SIGTSTP:
        os.kill(seller_pid.value,SIGUSR1)

def seller_handler(sig,frame):
    
    if sig == SIGINT:
        os.kill(driver_pid.value,SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(driver_pid.value,SIGUSR2)
    elif sig == SIGUSR1:
        print("arrived the station")
    


def driver():
    driver_pid.value = os.getpid()
    print(os.getpid())
    print(driver_pid.value)
    time.sleep(0.5)
    signal(SIGTSTP,driver_handler)
    signal(SIGUSR1,driver_handler)
    signal(SIGUSR2,driver_handler)
    signal(SIGINT,SIG_IGN)
    signal(SIGQUIT,SIG_IGN)
    while True:
        pass

def ticket_seller():
    seller_pid.value = os.getpid()
    print(os.getpid())
    print(seller_pid.value)
    time.sleep(0.5)
    signal(SIGINT,seller_handler)
    signal(SIGQUIT,seller_handler)
    signal(SIGUSR1,seller_handler)
    signal(SIGTSTP,SIG_IGN)
    while True:
        pass

signal(SIGTSTP,SIG_IGN)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)

p1 = Process(target = driver)
p2 = Process(target = ticket_seller)
p1.start()
p2.start()
p1.join()
p2.join()