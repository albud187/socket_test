import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host1 = "10.0.0.37"
host2 = "10.0.0.221"
port = 1236

Socket1 = socket.socket()
Socket2 = socket.socket()

SOCKET_DICT = {host1:Socket1, host2:Socket2}

try:
    Socket1.connect((host1,port))
except:
    pass

try:
    Socket2.connect((host2,port))
except:
    pass

#what happens if connection cannot be established or if connection is lost?
#make it try again on a seperate thread
#create a function / class for new thread

def multi_threaded_connection((host,port), socket_obj):
    socket

    pass

for IP_addr in SOCKET_DICT.keys():
    connection((IP_addr,port), SOCKET_DICT[IP_addr])

msg = input("->")

while msg != 'q':
    Socket1.send(msg.encode())
    Socket2.send(msg.encode())
    msg = input("->")

Socket1.close()
Socket2.close()

while True:
    start_new_thread(multi_threaded_connection, )
