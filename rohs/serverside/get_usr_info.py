def get_usr_info(list_of_terms : list, can_be_int = False, can_be_string = True, list_in = None, replay_times = 1):
    """will get usr info for things"""

    
    list1 = list()

    restart_list = False
    for i in range(0,replay_times):

        usr_input = input(list_of_terms[i])
        
    
        if list_in==None: list_in=[usr_input]; restart_list = True


        try:
            if can_be_int==True: usr_input = int(usr_input)
        except:
            pass

        
        
        if (can_be_int==False and isinstance(usr_input, int)) or (int(usr_input not in list_in) or not can_be_string and isinstance(usr_input, str)):
            return get_usr_info(list_of_terms,can_be_int, can_be_string, list_in, replay_times);
        

        else:
            list1.append(usr_input)

        if restart_list ==True: list_in=None

    return list1
        
