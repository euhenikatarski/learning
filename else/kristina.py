from datetime import date

class Kristina():

    def __init__(self, name, second_name, birth_year, birth_month, birth_day):

        self.name = name.title()
        self.second_name = second_name.title()
        self.birth_date = date(birth_year, birth_month, birth_day)


    def about_kristina(self):

        x = f'{self.name}, {self.second_name}, {self.age}'
        return x


    def birthday(self):

        actual_date = date.today()
        birthday_date = date(1998, 12, 23)
        if actual_date.day == birthday_date.day and actual_date.month == birthday_date.month:
            print(f'С днем Рождения {self.name}')
        else:
            print('Пока не ДР')
        print(actual_date)

    @property
    def age(self):

        today = date.today()
        years = today.year - self.birth_date.year
        if ((today.month, today.day) <
            (self.birth_date.month, self.birth_date.day)):
            years -= 1
        return years

kristina = Kristina('kris', 'zakharova', 2000, 7, 28)
print(kristina.about_kristina())
kristina.birthday()

print(kristina.name, kristina.second_name, kristina.age)

