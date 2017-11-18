from multiprocessing import Process, Event
import time


def wait_for_event(e):
    print("wait_for_event: starting",)
    e.wait() # 不超时，阻塞
    print("wairt_for_event: e.is_set()->" + str(e.is_set()))


def wait_for_event_timeout(e, t):
    print("wait_for_event_timeout:starting")
    e.wait(t) # 设置超时
    print("wait_for_event_timeout:e.is_set->" + str(e.is_set()))


if __name__ == "__main__":
    e = Event() # Event用来实现进程间同步通信
    w1 = Process(name="block", target=wait_for_event, args=(e,))
    w2 = Process(name="non-block", target=wait_for_event_timeout, args=(e, 2))

    w1.start()
    w2.start()

    time.sleep(3) # 3s后wait_for_event_timeout 超时， wait_for_event 得到event事件

    e.set() # 设置event
    print("main: event is set")
