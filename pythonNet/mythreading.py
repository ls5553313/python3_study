# mythreading.py


from threading import Thread
from time import sleep

class MyThreading(Thread):
    def __init__(self,target = None,args = None):
        self.target = target
        self.args = args
        super().__init__()

    def run(self):
        print("asdasdadasd")
        self.target(*self.args)

def player(song,sec):
    for i in rang(3):
        i = print("**********",song)
        sleep(sec)

t = MyThreading(target = player, args = ("dddd",2))
t.start()
t.join()