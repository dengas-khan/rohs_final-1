import socket
from file_info import file_info

file_coordinator = file_info()

HOST = "109.228.54.161"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))


server.listen(5)

while True:

    
    client, addr = server.accept()
    recvmsg = client.recv(1024)
    print(recvmsg.decode('ascii'))
    
    client.send(file_coordinator.return_final(recvmsg, addr[0]).encode('ascii'))

    client.close()
