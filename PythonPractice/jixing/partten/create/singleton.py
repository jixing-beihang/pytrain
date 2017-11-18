'''
单例模式的优点：
1、由于单例模式要求在全局内只有一个实例，因而可以节省比较多的内存空间；
2、全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用；
3、单例可长驻内存，减少系统开销。
单例模式的应用举例：
1、生成全局惟一的序列号；
2、访问全局复用的惟一资源，如磁盘、总线等；
3、单个对象占用的资源过多，如数据库等；
4、系统全局统一管理，如Windows下的Task Manager；
5、网站计数器。
单例模式的缺点
1、单例模式的扩展是比较困难的；
2、赋于了单例以太多的职责，某种程度上违反单一职责原则（六大原则后面会讲到）;
3、单例模式是并发协作软件模块中需要最先完成的，因而其不利于测试；
4、单例模式在某种情况下会导致“资源瓶颈”。
'''


import threading
import time


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            return super(Singleton, cls).__new__(cls, *args, **kwargs)

        # if not hasattr(cls, '_instance'):
        #     orig = super(Singleton, cls)
        #     cls._instance = orig.__new__(cls, *args, **kwargs)
        # return cls._instance


class Bus(Singleton):
    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print('Sending signal Data...', data)
        self.lock.release()


class VisitEntity(threading.Thread):
    my_bus = ''
    name = ''

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)


if __name__ == '__main__':
    for i in range(3):
        print('Entity %d begin to run ...' % i)
        my_entity = VisitEntity()
        my_entity.setName('Entity_' + str(i))
        my_entity.start()