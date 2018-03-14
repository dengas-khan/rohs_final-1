class file_info:


    def __init__(self, filename):
        """will create a file if there
           is no file that already exists"""

        try:
            self.file = open(filename, "r+")
            
        except:
            self.file = open(filename, "xt")
            self.file.close()
            
            self.file = open(filename, "r+")

            
    def write_info_to_file(self, username=None, password=None, ip=None):
        """parameteres will be strings. The information
           will be written to a file (if such a file exists)
           if not, a different"""


        self.file.append(username+password+'\n')


        return 'welcome to displacer the gathering' + username + '\r\n'


    def see_if_user_is_in_database(self, username):
        """this function will check to see if the user's ip
           is in the file"""


        if username in self.file.read(): return True

    
    def find_username_in_file(self, username, password):
        """will find the line for the username
           in the file"""
           
           
        if username + ' ; '+password in self.file.read():
            
            return True
          
        
        return False
        
        
    def return_final(self, username : str, ip : str):
        """will return the final descision of if
           the user is in the file"""


        if self.see_if_user_is_in_database(username): return 'welcome back ' + username + '\r\n'

        else: return write_to_file(username, ip)

                    
