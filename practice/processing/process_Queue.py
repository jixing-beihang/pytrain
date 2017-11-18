from multiprocessing import Process,Queue

def writer_proc(q):
    try:
        q.put(1,block=False)
    except:
        pass

def reader_proc(q):
    try:
        print(q.get(block=False))
    except:
        pass

if __name__ == "__main__":
    q = Queue() # Queue实现多进程之间的数据传递
    writer = Process(target=writer_proc,args=(q,))
    writer.start()

    reader = Process(target=reader_proc,args=(q,))
    reader.start()

    writer.join()
    reader.join()