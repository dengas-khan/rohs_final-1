import socket
import file_info


"""databse handling daemon"""


server = "Database Handler"

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('109.228.54.161',7070))

serversocket.listen(5)

newuser = False

file = file_info.file_info('database.txt')



while True:
    """server loop"""
    
    
    client,addr = serversocket.accept()
    
    print('[*] recieved connection on '+server)
    
    msg = client.recv(1024)
    msg = msg.decode('ascii')
    
    
    if 'New User' in msg: 
        msg = msg.replace('New User', '')
        newuser=True
    
    
    exec('global tuple1; tuple1 ='+"msg");
    
    
    if newuser:
        """if newuser is true, then it will see if 
           the username exists in the file, and then 
           if it is not, it will write the username
           and the password into the file, seperated 
           by a semicolon, e.g. speed_demon ; ***"""
           
           
        if file.see_if_user_in_database(tuple1[0]): 
            client.send('username already taken'.encode('ascii'))
        
        else:
            file.write_info_to_file(str(tuple1[0]),' ; '+str(tuple1[1]))
            client.send("username and password accepted".encode('ascii'))
    
    else:
        
        if not file.find_username_in_file(str(tuple1[0]), str(tuple1[1])):
            client.send('username or password incorrect'.encode('ascii'))
        
        else:
            client.send("username and password accepted".encode('ascii'))
            client.close()