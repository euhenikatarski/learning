from pathlib import Path

path = Path('lessons/files and exceptions/learning_python.txt')
content = path.read_text(encoding='UTF-8')
content = content.replace('Python', 'C#')
content = content.strip()
print(content)

#lines = content.splitlines()

print(f'\n--------------------------------------------------------------\n')

for line in content.splitlines():
    print(line)


message = 'go home'
print(message.replace('go','dont go'))

print(f'\n--------------------------------------------------------------\n')

#name = input('Введите имя: ')
#path = Path('lessons/files and exeptions/guest.txt')
#path.write_text(name.title())


print(f'\n--------------------------------------------------------------\n')

contents = 'Список гостей: \n\n'

while True:
    name = input('Введите имя: ')
    path = Path('lessons/files and exceptions/guest_book.txt')
    #contents = 'Список гостей: \n'
    contents += f'\tHello {name.title()}\n'
    path.write_text(contents, encoding='UTF-8')
    
    quession = input('Продолжить? Y/N:  ')
    if quession.title() == 'N':
        break