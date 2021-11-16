import threading
from datetime import datetime
from time import sleep
import originpro as op

#critical section to access Origin
def write(tt, name):
    global row, wks
    data=[tt, name]
    wks.from_list2(data, row)
    row += 1
    
#must not do print or anything related to Origin GUI inside the thread function
def thread_task(lock, name):
    for _ in range(5):
        sleep(0.5)
        now = datetime.now()
        tt = now.strftime("%H:%M:%S.%f")[:-3]
        lock.acquire()
        write(tt, name)
        lock.release()

#global variables to be used inside thread task
wks=op.new_sheet()
row = 0
#we need to have criticlal section for any access to Origin
lock = threading.Lock()

t1 = threading.Thread(target=thread_task, args=(lock,'a'))
t2 = threading.Thread(target=thread_task, args=(lock,'b'))
t1.start()
t2.start()
t1.join()
t2.join()
print('complete')
