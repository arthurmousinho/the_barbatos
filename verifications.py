class User:
    def __init__(self,username, password, email, user_type):
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type


    def verify_username_on_names_file(self):
        names_file = open(f'database/{self.user_type}_data/{self.user_type}_list.txt', 'r')
        names_file_list = names_file.readlines()
       
        new = []
        for x in names_file_list:
            item = x
            for y in ['\n']:
                item = item.replace(y, "")
                new.append(item)
            names_file.close()
        if self.username in new:
            return True
        else:
            return False


    def verify_user_email(self):
        try:
            user_file = open(f'database/{self.user_type}_data/{self.username}.txt', 'r')
        except(FileNotFoundError):
            return False
        else:
            email_formated = f"{self.email}\n"
            if user_file.readline() == email_formated:
                user_file.close()
                return True
            else:
                user_file.close()
                return False
        
    
    def verify_user_password(self):
        try:
            user_file = open(f'database/{self.user_type}_data/{self.username}.txt', 'r')
        except(FileNotFoundError):
            return False
        else:
            user_email = user_file.readline()
            user_password = user_file.readline()
            user_password_formated = user_password.rstrip('\n')
            
            if user_password == self.password:
                user_file.close()
                return True
            elif user_password_formated == self.password:
                user_file.close()
                return True
            else:
                user_file.close()
                return False
            