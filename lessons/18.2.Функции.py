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


