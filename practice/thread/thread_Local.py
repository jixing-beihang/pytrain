# ThreadLocal 解决了参数在一个线程中各个函数之间互相传递的问题

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, name='Thread-A', args=('Alice',))
t2 = threading.Thread(target=process_thread, name='Thread-B', args=('Jimmy',))

t1.start()
t2.start()
t1.join()
t2.join()
