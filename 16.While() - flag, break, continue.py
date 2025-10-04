pizza_toppings = ''

while pizza_toppings != 'quit':
    pizza_toppings = input('Введите топинг:')
    print(pizza_toppings)

print('\n-------------------------------------------------------------')

active = True
while active:
    age = input('Введите возраст:')
    age = int(age)
    if age < 3:
        print('Вход бесплатный')
        active = False
    elif age >= 3 and age <= 12:
        print('С вас 10 долларов')
        active = False
    elif age > 12 and age <= 80:
        print('С вас 15 долларов')
        active = False
    elif age > 80:
        print('Возраст не подходит')
        active = False

print('\n-------------------------------------------------------------')

while True:
    toppings = input('Топинг:')
    if toppings == 'quit':
        break
    else:
        print(toppings)

print('\n-------------------------------------------------------------')

age = 0

while age < 10:
    age += 1
    if age % 2 == 0:
        continue
    print(age)

