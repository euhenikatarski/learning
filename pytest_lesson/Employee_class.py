class Employee():

    def __init__(self, first, second, money):

        self.first_name = first
        self.second_name = second
        self.money = money


    def give_raise(self, money_raise=''):
        self.money = self.money
        if money_raise:
            self.money += money_raise
        else:
            self.money += 5000


    def show_money(self):
        print(f'{self.money}')


#oleg = Employee('Oleg', 'Olegovich', 1000)

#oleg.give_raise(100)

#oleg.show_money()
