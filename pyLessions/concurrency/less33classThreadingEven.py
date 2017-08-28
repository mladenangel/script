import time
import threading 
from colorama import *

class Worker(threading.Thread):
    def __init__(self,name,signal):
        threading.Thread.__init__(self)
        self.name=name
        self.signal=signal
    def run(self):
        print(Fore.RED+Back.WHITE+'waiting from',self.name)
        self.signal.wait()
        print('processing from',self.name)
        time.sleep(4)
        print('done from',self.name+Style.RESET_ALL)

signal_event = threading.Event()
my_thread1 = Worker('Thread1',signal_event)
my_thread1.setDaemon(True)
my_thread2 = Worker('Thread2',signal_event)
my_thread2.setDaemon(True)
my_thread3 = Worker('Thread3',signal_event)
my_thread3.setDaemon(True)
my_thread1.start()
my_thread2.start()
my_thread3.start()
time.sleep(10)
print(Fore.RED+Back.YELLOW+'Send a signal to start processing'+Style.RESET_ALL)
signal_event.set()
input('Press Enter to stop...')
print('Done all')
