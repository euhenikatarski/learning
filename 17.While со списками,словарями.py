print('\n-----------------------------------------------\n')

sandwich_orders = ['sandwich','buter','pastrami','pastrami','zapek','upro','pastrami']
#Удаляем из списка 'pastrami' навсегда
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

finished_sandwiches = []
#В этом цикле мы убираем готовые сендвичи метолом pop(), и добавляем из списка 
#pooped() - удаленных сендвичей, сендвичи в переменную sandwiches. После этого
#добавляем готовые сендвичи в список finished_sandwiches и выводим готовые сендвичи
#методом print()
while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f'Приготовленные: {sandwiches}')
    finished_sandwiches.append(sandwiches)
print('Готовые сендвичи:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

print(f'{finished_sandwiches}')

print('\n-----------------------------------------------\n')
#Задаем пустой словарь в который будем складывать ответы пользователей
responses = {}
#Создаем переменную которую будем искользовать как flag для завершения цикла
polling_active = True
#Просим ввести имя и место, далее сохраняем ответ в словаре responses[name] = place
#Создаем переменну repeat для возможности выхода из цикла при написании 'no'
#далее берем ключ:значение из списка responses, присваиваем им переменные и 
#выводим методом print()
while polling_active:
    name = input('\nВведите имя: ')
    place = input('Если бы вы могли посетить одно место, какое бы оно было?: ')
    responses[name] = place
    repeat = input('Хотите добавить еще что-то? yes/no: ')
    if repeat == 'no':
        polling_active = False
print(f'--- Poll Responses ---')
for name, place in responses.items():
    print(f'{name} хотел бы отдохнуть в {place}')