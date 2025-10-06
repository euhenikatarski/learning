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

def make_album(song_author, song_name, song_time = ''):
    song_info = {'author': song_author, 'song': song_name, 'time': song_time}
    return song_info
song = make_album('Скриптонит','Притон')
song_1 = make_album('ATL','Танцуйте')
song_2 = make_album('Scorpions','Humanity','5:20')
print(f'{song},\n{song_1},\n{song_2}')

print('\n-----------------------------------------------\n')

while True:
    author = input('Введите имя автора: ')
    if author == 'q':
        break
    song_enter = input('Введите название песни: ')
    if song_enter == 'q':
        break
    quit = input('Введите "q" для выхода: ')
    if quit == 'q':
        break
author_song = make_album(author,song_enter)
print(author_song)

print('\n-----------------------------------------------\n')

list = ['hello','bb','koko','shosho']

def show_messages(messages):
    for x in messages:
        msg = f'Сообщение: {x.title()}'
        print(msg)


    