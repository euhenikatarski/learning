#Здороваемся с admin по особенному, остальным стандартный ответ
person_names = ['admin','alex','gosha','kris','jenya']
for person_name in person_names:
    if person_name == 'admin':
        print('Привет, admin, посмотрим статистику?')
    else:
        print(f'Привет {person_name}, как дела?')

print('\n-------------------------------------------------------------\n')

#Проверяем что список пуст, выводим else, если добавить имя в список будет if
person_second_names = []
if person_second_names:
    for person_second_name in person_second_names:
        print(f'Привет {person_second_name}, как дела?')
else:
    print(f'Нужно добавить пользователя')

print('\n-------------------------------------------------------------\n')

current_users = ['dima','masha','gosha','kris','jenya','victor']

#Скопировали список в Upper формате
#upper_current_users = []
#for current_user in current_users:
#    current_user = current_user.upper()
#    upper_current_users.append(current_user)
#print(upper_current_users)

new_users = ['DIMA','kolya','egor','jora','fil','viCtor']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'{new_user.title()} вам нужно сменить имя')
    else:
        print(f'{new_user.title()} добро пожаловать!')

print('\n-------------------------------------------------------------\n')

numbers = list(range(1,10))
print(numbers)
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
print('Success')