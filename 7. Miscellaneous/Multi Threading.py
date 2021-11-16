import threading
from datetime import datetime
from time import sleep
import originpro as op

#critical section to global data
def write(tt, name):
    global v1, v2
    v1.append(name)
    v2.append(tt)
    
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
v1=[]
v2=[]
#we need to have criticlal section for any access to shared data
lock = threading.Lock()

t1 = threading.Thread(target=thread_task, args=(lock,'a'))
t2 = threading.Thread(target=thread_task, args=(lock,'b'))
t1.start()
t2.start()
t1.join()
t2.join()

#threads done, we can put data to a worksheet
wks=op.new_sheet()
#need to set col(2) as time format before putting data into it
wks.cols = 2
wks.as_time(1, 10)

wks.from_list(0, v1, 'Name')
wks.from_list(1, v2, 'Time')
