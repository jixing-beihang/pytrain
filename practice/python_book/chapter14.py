# coding: utf-8
# socket 编程
import socket
from socketserver import StreamRequestHandler, TCPServer


# s = socket.socket()
# host = 'localhost'
# port = 1234
# address = (host,port)
#
# s.bind(address)
# s.listen(10)
#
# while True:
#     c,req_addr = s.accept()
#     print('Got connection from',req_addr)
#     c.send(b'Server sent message...')
#     print(c.recv(1024))
#     c.close()


class Handler(StreamRequestHandler):
    def handle(self):
        req_addr = self.request.getpeername()
        print('Got connection from', req_addr)
        self.wfile.write(b'Thank you...')
        print(self.rfile.read(1024))


server = TCPServer(('localhost', 1234), Handler)
server.serve_forever()
