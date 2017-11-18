# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

print('Connect to server ...')
# 端口和验证码注意保持与task_master.py设置的完全一致:
manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d ... ' % (n, n))
        r = n * n
        time.sleep(1)
        result.put(r)
    except queue.Queue.empty():
        print('task queue is empty..')

print('worker exit ...')
