from user_class import User

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
