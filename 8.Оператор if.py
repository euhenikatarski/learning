cars = ['audi','mersedes','bmw','subaru']
car = 'audi'
if car in cars:
    print(f'{car} - доступна для покупки')

print('\n-------------------------------------------------------------\n')

age_1 = 15
age_2 = 18
if age_1 >= 15:
    print(f'{age_1} - подходящий возраст')

print('\n-------------------------------------------------------------\n')

#Оператор or подразумевает что одно условие должна подходить
age_3 = 25
if age_3 >= 18 or age_3 <=22:
    print("True")
else:
    print("False")

#Оператор and подразумевает все условия должны подходить
age_3 = 18
if age_3 >= 18 and age_3 <=22:
    print("True")
else:
    print("False")

print('\n-------------------------------------------------------------\n')

planets = ['mars','earth','mercury','venera']
if 'mars' in planets:
    print('Mars - есть в списке')
else:
    print('Mars - нет в списке')