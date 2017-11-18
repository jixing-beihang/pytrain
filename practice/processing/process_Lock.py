from multiprocessing import Lock, Process


def worker_with(lock, f):
    with lock:
        with open(f, 'a+') as fs:
            n = 10
            while n > 1:
                fs.write('Locked acquired via with\n')
                n -= 1


def worker_no_with(lock, f):
    lock.acquire()
    try:
        fs = open(f, 'a+')
        n = 10
        while n > 1:
            fs.write('Locked acquired directly\n')
            n -= 1
        fs.close()
    finally:
        lock.release()


if __name__ == "__main__":
    lock = Lock()
    f = "file.txt"
    w = Process(target=worker_with, args=(lock, f))
    nw = Process(target=worker_no_with, args=(lock, f))

    w.start()
    nw.start()

    w.join()
    nw.join()
    print("end")
