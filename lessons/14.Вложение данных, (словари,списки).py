person_0 = {
    'first_name': 'Alex',
    'last_name': 'Shmaleks',
    'age': 25,
    'city': 'Homel',
    }
person_1 = {
    'first_name': 'Oleg',
    'last_name': 'Kasta',
    'age': 15,
    'city': 'Homel',
    }
person_2 = {
    'first_name': 'Dima',
    'last_name': 'Malik',
    'age': 56,
    'city': 'Minsk',
    }
#Добавляем словари в список
peoples = [person_0, person_1, person_2]
#Перебираем и выводим словари из списка
for people in peoples:
    print(f'{people}')

print('\n-------------------------------------------------------------\n')

cat = {
    'name': 'Gosh',
    'owner': 'Dima',
    }
dog = {
    'name': 'Boba',
    'owner': 'Katya',
    }
#Добавляем словари в список
pets = [cat, dog]
#Забираю из списка pets[] второй индекс [dog]
for pet in pets[1:2]:
    #Создаю переменную dog_name и заполняю ее значением ключа 'name'
    dog_name = f'{dog['name']}'
    print(f'Собака по кличке:\n\t{dog_name}')
    #Создаю переменную dog_owner и заполняю ее значением ключа 'owner'
    dog_owner = f'{dog['owner']}'
    print(f'Хозяин:\n\t{dog_owner}')
print('')
for pet in pets[:1]:
    cat_name = f'{cat['name']}'
    print(f'Кот по кличке:\n\t{cat_name}')
    cat_owner = f'{cat['owner']}'
    print(f'Хозяин:\n\t{cat_owner}')

print('\n-------------------------------------------------------------\n')

favorite_places = {
    'john'  : ['moscow', 'krasnoyarks'],
    'peter' : ['sweden', 'mayami'],
    'ivan'  : ['kaliningrad', 'everest']
}
#Создаю переменные для ключа(name), значения(places) методом items()
for name, places in favorite_places.items():
    #Вывожу переменную name с ключами (john,peter,ivan)
    print("\n" + name.title() + "`s favorite places is: ")
    #Создаю переменную place для значений из списка places
    for place in places:
        #Вывожу все элементы place
        print("\t" + place.title())

print('\n-------------------------------------------------------------\n')

numbers = {
    'alex': [7,9,12],
    'dima': [1,8,9,0],
    'eva': [90,65,123],
    'kris': [19],
    'jenya': [8],
}

for names, values in numbers.items():
    print(f'\n{names.title()} - любимые числа это:')
    for value in values:
        print(f'\t{value}')

for name in numbers['alex']:
    print(f'\n{name}')

print('\n-------------------------------------------------------------\n')

cities = {
    'minsk': {
        'population': '2000000',
        'country': 'Belarus',
        'fact': 'LOHI',
    },
    'homel': {
        'population': '500000',
        'country': 'Belarus',
        'fact': 'TOP',
    },
    'vitebsk': {
        'population': '500000',
        'country': 'Belarus',
        'fact': 'NOT BAD',
    }
}

for city_name, city_info in cities.items():
    print(f'\n{city_name} - Город')
    info = f'\n\t{city_info['population']} \n\t{city_info['country']} \n\t{city_info['fact']}'
    print(f'Информация о городе:\t {info}')
