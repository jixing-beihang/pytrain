'''
优点:
1、职责清晰：非常符合单一职责原则，主题对象实现真实业务逻辑，而非本职责的事务，交由代理完成；
2、扩展性强：面对主题对象可能会有的改变，代理模式在不改变对外接口的情况下，可以实现最大程度的扩展；
3、保证主题对象的处理逻辑：代理可以通过检查参数的方式，保证主题对象的处理逻辑输入在理想范围内。
应用场景：
1、针对某特定对象进行功能和增强性扩展。如IP防火墙、远程访问代理等技术的应用；
2、对主题对象进行保护。如大流量代理，安全代理等；
3、减轻主题对象负载。如权限代理等。
代理模式的缺点
1、可能会降低整体业务的处理效率和速度。
'''

info_struct = dict()
info_struct['addr'] = 10000
info_struct['content'] = 'starting...'


class Server():
    content = ''

    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self):
        pass


class InfoServer(Server):
    def recv(self, info):
        self.content = info
        return 'recv ok'

    def send(self, info):
        pass

    def show(self):
        print('show:%s' % self.content)


class ServerProxy():
    pass


class InfoServerProxy(ServerProxy):
    server = ''

    def __init__(self, server):
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(InfoServerProxy):
    whilte_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except Exception as e:
            return 'info structure is not correct'
        addr = info.get('addr', 0)
        if not addr in self.whilte_list:
            return 'your address is not in the white list'
        else:
            content = info.get('content', '')
            return self.server.recv(content)

    def addWhite(self, addr):
        self.whilte_list.append(addr)

    def removeWhite(self, addr):
        self.whilte_list.remove(addr)

    def clearWhite(self):
        self.whilte_list = []


if __name__ == '__main__':
    info_struct = dict()
    info_struct['addr'] = 10010
    info_struct['content'] = 'Hello World'
    info_server = InfoServer()
    info_server_proxy = WhiteInfoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()

    info_server_proxy.addWhite(10010)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
