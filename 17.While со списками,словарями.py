print('\n-----------------------------------------------\n')

sandwich_orders = ['sandwich','buter','pastrami','pastrami','zapek','upro','pastrami']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

finished_sandwiches = []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f'Приготовленные: {sandwiches}')
    finished_sandwiches.append(sandwiches)
print('Готовые сендвичи:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

print(f'{finished_sandwiches}')

print('\n-----------------------------------------------\n')

responses = {}
polling_active = True

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