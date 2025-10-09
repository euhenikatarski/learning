class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_surved = 0

    def describe_restaurant(self):

        print(f'{self.restaurant_name} - название ресторана')
        print(f'{self.cuisine_type} - вид кухни')
        print(f'{self.number_surved} - кол-во заказов')

    def open_restaurant(self):

        print(f'Ресторан открыт')

    def set_number_surved(self, set_number):

        self.number_surved = set_number

    def read_set_number(self):

        print(f'{self.number_surved} - кол-во заказов')

    def increment_number(self, number):
        
        self.number_surved += number

restaurant_3 = Restaurant('Грань','Пивная')
restaurant_3.number_surved = 98
restaurant_3.set_number_surved(98)
restaurant_3.describe_restaurant()
restaurant_3.increment_number(76)
restaurant_3.describe_restaurant()

print(f'\n-------------------------------------------------------------\n')

restaurant = Restaurant('Ирина','Итальянская')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_surved = 15
restaurant.describe_restaurant()
restaurant.set_number_surved(88)
restaurant.read_set_number()
restaurant.describe_restaurant()

print(f'\n-------------------------------------------------------------\n')

restaurant_1 = Restaurant('Батьки','Народная')
restaurant_1.number_surved = 99
restaurant_1.describe_restaurant()


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
              f'Last name - {self.last_name.title()}, age - {self.age}, sex - {self.sex} '                  f'Online - {self.login_attempts}' 
            )
    
    def greet_user(self):
        
        print(f'Hello, {self.first_name.title()} {self.second_name.title()}!')


print(f'\n-------------------------------------------------------------\n')

user_3 = User('Oleg','Predik')
user_3.increment_login_attempts()
user_3.describe_user()
user_3.reset_login_attempts()
user_3.describe_user()

            

print(f'\n-------------------------------------------------------------\n')

user = User('kristina', 'perdina')
user.describe_user()
user.greet_user()

print(f'\n-------------------------------------------------------------\n')

user_2 = User('aleg','maleg','kalek', '28', 'male')
user_2.describe_user()