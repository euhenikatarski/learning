names = ['Alex','Peter','Gosha',]
#Здороваемся с первым из списка
message = f"Я бы хотел дружить с {names[0].title()}"
print(message)

print('\n-------------------------------------------------------------\n')
# Зовем всех пить пиво от 0 до 3 смещение 1 индекс
persons = ['Alex','Dima','Tima','Cat']
message = f'Привет,{persons[0].title()}, приходи пить пиво'
message_1 = f'Привет,{persons[1].title()}, приходи пить пиво'
message_2 = f'Привет,{persons[2].title()}, приходи пить пиво'
message_3 = f'Привет,{persons[3].title()}, приходи пить пиво'
print(persons)
print(message)
print(message_1)
print(message_2)
print(message_3)

print('\n-------------------------------------------------------------\n')
#pop(0)-выгоняет первого из списка и сохраняет информацию о нем в popped_persons
popped_persons = persons.pop(0)
print(popped_persons)  #выводим выгнаного гостя
print(persons)
persons[1] = 'Oleg'  #меняем в спикске индекс 1 на Олег, был Тима стал Олег
print(persons)
message_1 = f'Привет,{persons[0].title()}, приходи пить пиво'
message_2 = f'Привет,{persons[1].title()}, приходи пить пиво'
message_3 = f'Привет,{persons[2].title()}, приходи пить пиво'
print(persons)
print(message_1)
print(message_2)
print(message_3)

print('\n-------------------------------------------------------------\n')

print('Я нашел стол большего размера')
#Добавляем Веру на индекс 0 в список, все индексы сместились на 1 вправо
persons.insert(0, 'Vera')
#Добавляем Веру на индекс 0 в список, все индексы от 2 до конца сместились на 1 вправо
persons.insert(2, 'Tolik')
persons.append('georgi') #Добавляем в конец списка
print(persons)

print('\n-------------------------------------------------------------\n')

print('К сожалению придут только 2 гостя')
popped_persons = persons.pop()  #Убираем из списка человека под индексом 0, первого слева
print(f'Извини {popped_persons.title()}, ужина не будет')
popped_persons = persons.pop()  #Убираем из списка человека под индексом 0, первого слева
print(f'Извини {popped_persons.title()}, ужина не будет')
popped_persons = persons.pop()  #Убираем из списка человека под индексом 0, первого слева
print(f'Извини {popped_persons.title()}, ужина не будет')
popped_persons = persons.pop()  #Убираем из списка человека под индексом 0, первого слева
print(f'Извини {popped_persons.title()}, ужина не будет')
print(persons)

print(f'{persons[0]}, сообщаю что ужин в силе')
print(f'{persons[1]}, сообщаю что ужин в силе')

print('\n-------------------------------------------------------------\n')

del persons[0] #удаляем человека под индексом 0 навсегда
del persons[0]
print(persons)