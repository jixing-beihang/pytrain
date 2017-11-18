# coding: utf-8
import socket

s = socket.socket()
host = 'localhost'
port = 1234
address = (host,port)

s.connect(address)
message = s.recv(1024)
print(message)
if message:
    print(message)
    s.send(b'Client received message...')