import time
from multiprocessing import Pipe, Process


def proc1(pipe):
    while True:
        for i in range(10000):
            print("proc1 send: %s" % (i))
            pipe.send(i)
            time.sleep(1)


def proc2(pipe):
    while True:
        print("proc2 recv:", pipe.recv())
        time.sleep(1)


if __name__ == "__main__":
    (read, write) = Pipe()  # 全双工 duplex
    print(read)
    p1 = Process(target=proc1, args=(read,))
    p2 = Process(target=proc2, args=(write,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
