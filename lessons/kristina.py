def check_drislo(name):
    if name.lower() == 'kristina':
        print(f'{name} - пердунья')
    else:
        print(f'Привет, {name}')

check_drislo(input('Enter name: '))
names = [
    'alex', 'maria', 'ivan', 'olga', 'sergey', 'daria', 'nikita', 'elena', 'andrey', 'svetlana',
    'pavel', 'irina', 'vladimir', 'anna', 'egor', 'natalia', 'roman', 'tatiana', 'denis', 'ekaterina',
    'maxim', 'valentina', 'artem', 'galina', 'konstantin', 'ludmila', 'stepan', 'veronika', 'boris', 'alla',
    'ilya', 'yana', 'vadim', 'viktoria', 'kristina', 'oksana', 'gennady', 'alina', 'leonid', 'sofia',
    'grigory', 'arina', 'dmitry', 'milana', 'stanislav', 'zoya', 'vasily', 'karina', 'yuriy'
]

def get_perdunya(*args):


    for name in args:
        name_lower = name.lower()
        if name_lower == 'kristina':
            print(f'{name_lower} - пердунья')
            break
        else:
            print(f'{name_lower} - не пердун')
            continue
    

get_perdunya('alex', 'maria', 'ivan', 'olga', 'sergey', 'daria', 'nikita', 'elena', 'andrey', 'svetlana',
    'pavel', 'irina', 'vladimir', 'anna', 'egor', 'natalia', 'roman', 'tatiana', 'denis', 'ekaterina',
    'maxim', 'valentina', 'artem', 'galina', 'konstantin', 'ludmila', 'stepan', 'veronika', 'boris', 'alla',
    'ilya', 'yana', 'vadim', 'viktoria', 'kristina', 'oksana', 'gennady', 'alina', 'leonid', 'sofia',
    'grigory', 'arina', 'dmitry', 'milana', 'stanislav', 'zoya', 'vasily', 'karina', 'yuriy')


