class Data:
    def __init__(self,username, password, email, user_type):
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type
    
    
    def add_username_on_names_list(self):
        add_names_list = open(f'database/{self.user_type}_data/{self.user_type}_list.txt' , 'a')
        add_names_list.write(f'\n{self.username}')
        add_names_list.close()


    def creat_client_file(self):
        creat_client_file = open(f'database/{self.user_type}_data/{self.username}.txt' , 'x')
        creat_client_file.close()


    def add_data_on_client_file(self):
        file =  open(f'database/{self.user_type}_data/{self.username}.txt' , 'a')
        file.write(self.email)
        file.write(f'\n{self.password}')
        file.close()