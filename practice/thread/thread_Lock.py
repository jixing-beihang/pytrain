import threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()  # 创建一个线程锁


def change(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()  # 只有一个线程能成功地获取锁
        try:
            change(i)
        finally:
            lock.release()  # 最后释放线程锁
        # change(i)


t1 = threading.Thread(target=run_thread, name='change5', args=(5,))
t2 = threading.Thread(target=run_thread, name='change8', args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)
