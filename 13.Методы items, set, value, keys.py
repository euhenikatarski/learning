
glossarii = {
    'Словарь': 'В языке Python словарь представляет собой пару ключ : значение',
    'Список': 'В списках Python можно заменять элементы списка в отличии от Кортежа',
    'Переменная': '(variable) — имя, которое ссылается на значение в памяти.',
    'Функция': '(function) — блок кода, который можно вызвать по имени и использовать повторно.',
    'Цикл': '(loop) — конструкция для повторения действий.',
    'Класс': '(class) — шаблон для создания объектов с определёнными свойствами и методами',
}
for termin, text in glossarii.items():
    print(f'{termin} - {text}')

print('\n-------------------------------------------------------------\n')

#Метод items() возвращает пару ключ:значение из словаря rivers
rivers = {
    'Amazonka': 'Brazilia',
    'Volga': 'Russia',
    'Sena': 'France',
}
for river, country in rivers.items():
    print(f'{river} течет в {country}')

print('\n-------------------------------------------------------------\n')

#Метод keys() возвращает ключ из словаря rivers
for river in rivers.keys():
    print(f'{river} - река')
#Метод keys() можно не писать, но лучше писать для удобочитаемости
for river in rivers:
    print(f'{river} - река 1')

print('\n-------------------------------------------------------------\n')

#Метод values() возвращает значение из словаря rivers
for country in rivers.values():
    print(f'{country} - страна')

print('\n-------------------------------------------------------------\n')

favorite_languages = {
    'alex': 'Python',
    'dima': 'C++',
    'eva': 'Java',
    'kris': 'JavaScript',
    'jenya': 'JavaScript',
}
#Проверяем что люди из списка прошли участиве в опросе, словарь favorite_languages
names = ['vera','tanya','grisha','alex','dima']
for name in names:
    if name in favorite_languages.keys():
        print(f'{name} - спасибо что прошел опрос')
    else:
        print(f'{name} - пройди опрос')

print('\n-------------------------------------------------------------\n')

#Убираем дубликаты из словаря favorite_languages методом set()
for languages in set(favorite_languages.values()):
    print(languages.title())