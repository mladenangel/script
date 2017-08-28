import time
import threading
from colorama import *

class MyThread(threading.Thread):
    def __init__(self,name,o_lock):
        threading.Thread.__init__(self)
        self.name = name
        self.running = False
        self.value_lock = o_lock

    def run(self):
        global value
        self.running = True
        while self.running:
            self.value_lock.acquire()
            value += 1
            print(Fore.RED+Back.WHITE+'value:',str(value),'from',self.name+Style.RESET_ALL)
            self.value_lock.release()
            time.sleep(2)
    def stop(self):
        print(Fore.RED+Back.YELLOW+'stopping',self.name+Style.RESET_ALL)
        self.running = False
        self.join(2)
global value
value = 0
value_lock = threading.Lock()
my_thread1=MyThread('Thread1',value_lock)
my_thread1.setDaemon(True)
my_thread2=MyThread('Thread2',value_lock)
my_thread2.setDaemon(True)
my_thread1.start()
my_thread2.start()
input('Press Enter to stop..')

my_thread1.stop()
my_thread2.stop()

