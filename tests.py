message = 'выход' #здесь ''
#Цикл while будет повторяться пока в message не будет значения 'выход'
while message != 'выход':
#    message = input('Выйти напиши: ')
    if message != 'выход':
        print(f'{message}')

print('\n-------------------------------------------------------------\n')


integer = 9 #здесь ''

while integer != 9:
#    integer = input('Угадай число от 1 до 9:')
#integer = int(integer)
    if integer != 9 and integer >= 100:
        print(f'{integer} - далеко ушел')
    elif integer != 9 and integer >= 50 and integer < 100:
        print(f'{integer} - бери меньше')
    elif integer == 9:
        print(f'Угадал - {integer}')

print('\n-------------------------------------------------------------\n')

figures_1 = {
    'krug': 'belii',
    'oval': 'yellow',
    'kvadrat': 'green',
    'treyg': 'dark',
    'dodekaedr': 'dark',
    'romb': 'pink',
}
figures_3 = {
    'krug': 'belii',
    'oval': 'yellow',
    'kvadrat': 'green',
    'treyg': 'dark',
    'dodekaedr': 'dark',
    'romb': 'pink',
}

figures_1['pallelagram'] = 'yellow' #добавляем пару ключ:значение
print(figures_1)
del figures_1['krug'] #удаляем ключ:значение по ключу
print(figures_1)
figures_1['oval'] = 'krasnii' #меняем значение для ключа oval
print(figures_1)

print('\n-------------------------------------------------------------\n')

figures_2 = {
    'krug': 'belii',
    'oval': 'yellow',
    'kvadrat': 'green',
    'treyg': 'dark',
    'dodekaedr': 'dark',
    'romb': 'pink',
}

for figures, colors in figures_2.items():
    figure = f'{figures} - фигура'
    color = f'{colors} - цвет'
    print(f'{figure}\n\t{color}')

print('\n-------------------------------------------------------------\n')

persons_tickets = {
    'alex': {
        'first_name': 'Alex',
        'second_name': 'Piligrim',
        'animal': 'cat',
        'male': 'man',
    },
    'masha': {
        'first_name': 'Masha',
        'second_name': 'Piligrim',
        'animal': 'cat',
        'male': 'women',
    },
    'dima': {
        'first_name': 'Dima',
        'second_name': 'Lokit',
        'animal': 'dog',
        'male': 'man',
    },
}

for informations in persons_tickets.values():
    person = f'{informations['first_name']} {informations['second_name']}'
    info_about_person = f'\t{informations['animal']} - животное\n\t{informations['male']} - пол'
    print(f'{person}:\n{info_about_person}\n')