'''
# 创建单个的子进程 Process
from multiprocessing import Process
import os


def run_proc(name):
    print('child process %s (%s).' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('child will start...')
    p.start()
    p.join()
    print('child process end.')
'''

# 创建子进程池 Pool
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    # print(time.strftime('%Y%m%d%H%M%S',time.localtime()))
    print('Task %s runs %0.2f seconds' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(processes=4)
    for i in range(5):
        # p.apply_async(long_time_task,args=(i,)) # 非阻塞，apply_async
        p.apply(long_time_task,args=(i,)) # 阻塞，apply
    print('Waiting for all done...')
    p.close()
    p.join()
    print('All subprocess done.')
