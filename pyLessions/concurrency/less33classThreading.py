import time
import threading
from colorama import *

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = False
    def run(self):
        counter = 0
        self.running = True
        while self.running:
            print(Fore.RED+Back.YELLOW+'counter:',str(counter)+Style.RESET_ALL)
            time.sleep(2)
            counter += 1
    def stop(self):
        print(Fore.RED+Back.YELLOW+'stopping thread...'+Style.RESET_ALL)
        self.running = False
        self.join(2)

my_thread=MyThread()
my_thread.setDaemon(True)
my_thread.start()

input('Press Enter to stop...')
my_thread.stop()
