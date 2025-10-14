messages = ['2','3','4','5','6']
sent_messages = []

print(messages)
print(sent_messages)

def send_messages(messages, sent_messages):
    
    while messages:

        current_message = messages.pop()
        print(f'Отправлено: {current_message}')
        sent_messages.append(current_message)

#messages[:] позволяет оставить в списке message значения.
send_messages(messages[:], sent_messages)

#в этом варианте значения удаляются из списка messages
send_messages(messages, sent_messages)

print(messages)
print(sent_messages)

def completed_message(sent_message):
    for message in sent_messages:
        print(f'{message}')

completed_message(sent_messages)