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