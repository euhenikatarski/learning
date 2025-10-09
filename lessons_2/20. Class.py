class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f'{self.restaurant_name} - название ресторана')
        print(f'{self.cuisine_type} - вид кухни')

    def open_restaurant(self):

        print(f'Ресторан открыт')



restaurant = Restaurant('Ирина','Итальянская')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant_1 = Restaurant('Батьки','Народная')
restaurant_1.describe_restaurant()

class User:

    def __init__(self, first_name, second_name, last_name='', age='', sex=''):
        
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):

        if self.first_name and self.second_name and self.last_name and self.age and self.sex:

            print(
                  f'Name - {self.first_name.title()}, Second name - {self.second_name.title()}, '
                  f'Last name - {self.last_name.title()}, age - {self.age}, sex - {self.sex}'
                 )
        elif self.first_name and self.second_name:

            print(
                  f'Name - {self.first_name.title()}, Second name - {self.second_name.title()}'
                 )
    
    def greet_user(self):
        
        print(f'Hello, {self.first_name.title()} {self.second_name.title()}!')
            

user = User('kristina', 'perdina')
user.describe_user()
user.greet_user()

user_2 = User('aleg','maleg','kalek', '28', 'male')
user_2.describe_user()