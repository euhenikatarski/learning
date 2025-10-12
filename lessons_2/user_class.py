class User:

    def __init__(self, first_name, second_name, last_name='', age='', sex=''):
        
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def increment_login_attempts(self):
        
        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0

    def describe_user(self):

        print(
              f'Name - {self.first_name.title()}, Second name - {self.second_name.title()}, '
              f'Last name - {self.last_name.title()}, age - {self.age}, sex - {self.sex} '                  
              f'Online - {self.login_attempts}' 
            )
    
    def greet_user(self):
        
        print(f'Hello, {self.first_name.title()} {self.second_name.title()}!')


class Admin(User):

    def __init__(self, first_name, second_name, privileges, last_name='', age='', sex=''):
        super().__init__(first_name, second_name, last_name, age, sex)
        self.privileges = Privileges(privileges)


class Privileges():

    def __init__(self, privileges):
        
        self.privileges = privileges

    def show_privileges(self):
        
        print(f'Виды привелегий: ')
        for privilege in self.privileges:
            print(f'\t{privilege}')
