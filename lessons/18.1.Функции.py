from make_album import make_albums


def display_message():
    print('\nсоси пени')

display_message()

print('\n-----------------------------------------------\n')

def favorite_book(title):
    print(f'Книга - {title}')

favorite_book('Алиса в стране чудес')

print('\n-----------------------------------------------\n')

def make_shirt(shirt_size='L', shirt_text='I Love Python'):
    print(f'Размер - {shirt_size}, Текст - {shirt_text}')

make_shirt('32', 'Lacoste')
make_shirt(shirt_size='52',shirt_text='BMW')
make_shirt()
make_shirt('M','Luke')

print('\n-----------------------------------------------\n')

def describe_city(city, country='Belarus'):
    print(f'{city} находится в {country}')

describe_city('Homel')
describe_city('Minsk')
describe_city('Vitebsk')
describe_city(city='Moscow', country='Russia')

print('\n-----------------------------------------------\n')

def city_country(city,country):
    pair_city_contry = f'{city}, {country}'
    return pair_city_contry.title()
pair = city_country('Homel','Belarus')
print(pair)

print('\n-----------------------------------------------\n')

while True:
    author = input('Введите имя автора: ')
    song_enter = input('Введите название песни: ')
    quit = input('Еще раз? yes/no : ')
    if quit == 'no':
        author_song = make_albums(author, song_enter)
        break
    else:
        author_song = make_albums(author, song_enter)
#author_song = make_album(author,song_enter)
print(author_song)

print('\n-----------------------------------------------\n')

list = ['hello','bb','koko','shosho']

def show_messages(messages):
    for x in messages:
        msg = f'Сообщение: {x.title()}'
        print(msg)


    