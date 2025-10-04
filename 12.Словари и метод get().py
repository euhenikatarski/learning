person = {
    'first_name': 'Alex',
    'last_name': 'Shmaleks',
    'age': 25,
    'city': 'Homel',
    }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print('\n-------------------------------------------------------------\n')

numbers = {
    'alex': 7,
    'dima': 1,
    'eva': 9,
    'kris': 19,
    'jenya': 8,
}

number = numbers.get('alex')
print(f'{number} - число Alexa')

print('\n-------------------------------------------------------------\n')

glossarii = {
    'Словарь': 'В языке Python словарь представляет собой пару ключ : значение',
    'Список': 'В списках Python можно заменять элементы списка в отличии от Кортежа'
}
glossarii_1 = glossarii.get('Словарь')
print(f'Словарь - {glossarii_1}\n')
glossarii_2 = glossarii.get('Список')
print(f'Список - {glossarii_2}')
