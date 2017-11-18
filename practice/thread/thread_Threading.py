import time, threading


# 新线程执行
def loop():
    print('thread %s id running...' % threading.current_thread().name) # 子线程开始执行
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name) # 子线程结束执行


print('thread %s is running...' % threading.current_thread().name)  # 主线程开始运行

t = threading.Thread(target=loop, name='LoopThread', args=())
t.start()
t.join()

print('thread %s ended.' % threading.current_thread().name)  # 主线程结束运行
