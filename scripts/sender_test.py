import socket

def get_IP_info(filename):
    with open(filename) as f:
        lines = f.readlines()

    result_dict ={"HOST":lines[0].strip(), "PORT":int(lines[1].strip())}

    return result_dict
IP_INFO_FILE = "IP_DATA_SENDER.txt"
IP_INFO = get_IP_info(IP_INFO_FILE)
HOST = IP_INFO["HOST"]
PORT = IP_INFO["PORT"]

def Main():
    mySocket = socket.socket()
    mySocket.connect((HOST,PORT))

    message = input(" -> ")

    while message != 'q':
            mySocket.send(message.encode())
            #data = mySocket.recv(1024).decode()

            #print ('Received from server: ' + data)

            message = input(" -> ")

    mySocket.close()

Main()