import threading
from datetime import datetime
from time import sleep
import originpro as op

#critical section to global data
def write(tt, name):
    global colA, colB
    colA.append(name)
    colB.append(tt)
    
#must not do print or anything related to Origin inside the thread function
def thread_task(lock, name):
    for _ in range(5):
        sleep(0.5)
        now = datetime.now()
        tt = now.strftime("%H:%M:%S.%f")[:-3]
        lock.acquire()
        write(tt, name)
        lock.release()

#global variables to be used inside thread task
colA=[]
colB=[]
#we need to have criticlal section for any access to shared data
lock = threading.Lock()

t1 = threading.Thread(target=thread_task, args=(lock,'a'))
t2 = threading.Thread(target=thread_task, args=(lock,'b'))
t1.start()
t2.start()
t1.join()
t2.join()
wks=op.new_sheet()
wks.from_list(0, colA, 'Name')
wks.from_list(1, colB, 'time')

