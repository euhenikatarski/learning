from show import *
import show as s
from show import show_messages as sm
import show
from show import show_messages

messages = ['hi','hello','cucumber']

show_messages(messages)

print('\n------------------------------------------------------\n')

s.show_messages(messages)

print('\n------------------------------------------------------\n')

sm(messages)

print('\n------------------------------------------------------\n')

show.show_messages(messages)