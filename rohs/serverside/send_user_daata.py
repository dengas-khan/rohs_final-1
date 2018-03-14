import socket
from get_usr_info import get_usr_info


"""this will be the first socket to open, and will be used to sign  the player
   in. Later, we will use pygame to get the inputs and see if they want to sign
   in or not, but for now, I will just use the 'Input' function"""



print('1:    sign in')
print('')
print('2:    sign up')
print('')
print('3:    exit')


def get_spaces():
    usr_info = (get_usr_info(['enter your choice'],True, False, [1,2,3]))
    print(usr_info)
    return ['i'*(usr_info[0]-1), usr_info]


def sign_in():
    return get_usr_info(['enter your username', 'enter your password'], False, True, None, 2)




client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    

def send_data():
    """will send the
    client data"""


    user_pass = get_spaces()
    user_pass_=sign_in()
    client.connect(('109.228.54.161', 7070))
    
    if len(user_pass[0])==2:
        exit()
    
    
    else:
        
        client.send(('('+user_pass_[0]+','+user_pass_[1]+')'+(' New User' * len(user_pass[0]))+"\r\n").encode('ascii'))
    
    msg = client.recv(1024)
    
    if msg.decode('ascii')=="username and password accepted":
        exit()
    
    
    elif (msg.decode('ascii') == "username already taken") or (msg.decode('ascii')=="username or password incorrect"):
    
        while msg.decode('ascii')!="username and password accepted":
            user_pass = sign_in()
            client.send(('('+user_pass_[0]+','+user_pass_[1]+')'+(' New User' * len(user_pass[0]))+"\r\n").encode('ascii'))
            msg = client.recv(1024)
        
        
        exit()
  
        
send_data()