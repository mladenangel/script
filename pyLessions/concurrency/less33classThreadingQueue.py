import time
import threading
import queue
class Worker(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.name=name
        self.q=q
    def run(self):
        while True:
            if self.q.empty():
                print('thread stopped')
                break
            job=self.q.get()
            print('run job',str(job),'from',self.name)
            time.sleep(1)
            self.q.task_done()
q=queue.Queue()
print('populate jobs')
for i in range(15):
    q.put(i)

my_thread1=Worker('Thread1',q)
my_thread1.setDaemon(True)
my_thread2=Worker('Thread2',q)
my_thread2.setDaemon(True)
my_thread3=Worker('Thread3',q)
my_thread3.setDaemon(True)
my_thread1.start()
my_thread2.start()
my_thread3.start()
my_thread1.join()
my_thread2.join()
my_thread3.join()
input('Press Enter to stop...')
print('Done all')

