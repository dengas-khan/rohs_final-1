import socket

username = input('enter your username') 

HOST = '109.228.54.161'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
sendmsg = username
client.send(sendmsg.encode('ascii'))
msg = client.recv(1024)


client.close()
print(msg.decode('ascii')
    )
