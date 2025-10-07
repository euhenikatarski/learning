messages = ['hello','bb','koko','shosho']
print(messages)

#Создаем функцию с аргументом (message)
#далее цикл for создает переменную x в которую складываются значения из messages
#далее создаем переменную msg в которой храним x - значение из messages
def show_messages(messages):
    for x in messages:
        msg = f'Сообщение: {x.title()}'
        print(msg)

#Вызываем функцию для списка list
show_messages(messages)

sent_messages = []

#Создаем функцию с аргументом messages чтобы функцию можно было передавать
#send_message() - пустой аргумент выдаст ошибку
#далее в цикле while создается переменная current_message, которая забирает в себя 
#pop-нутое значение из передаваемой инфы(списка,словаря и тд)
#далее добавляем попнутое значение в список sent_messages
def send_messages(messages, sent_messages):

    while messages:
        current_message = messages.pop()
        print(f'Отправленные сообщения: {current_message}')
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)

#*args - создает пустой кортеж и упаковывает в него все полученные значения
def get_components(*args):
    print(*args)

get_components('cheese','bread','onion','tomato','salami')

#**kwargs - создает пустой словарь и упаковывает в него все полученные пары ключ:значение
def build_profile(first, second, **kwargs):
    kwargs['first_name'] = first
    kwargs['second_name'] = second
    return kwargs

user_profile = build_profile('Jenya', 'Meka', sex = 'male', color = 'white')
print(user_profile)


def save_info(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car_info = save_info('BMW','X5', color = 'red', tow_package = True)
print(f'\n{car_info}')