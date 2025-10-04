desc = ''
peoples = ['dodik','podij','sika']

print(peoples)
print(peoples[0])

for people in peoples[0:3]:
    if people == 'podij':
        print(f'{people} - соси пенис')
    else:
        print(f'{people} - тебе сказать нечего')

print('\n-----------------------------------------------\n')

favorite_places = {
    'adidas': {
        'size': '43',
        'color': 'red',
        'cost': '4,54',
        'model': 'blazer',
    },
    'puma': {
        'size': '44',
        'color': 'green',
        'cost': '4,54',
        'model': 'custom',
    },
    'nike': {
        'size': '46',
        'color': 'yellow',
        'cost': '4,99',
        'model': 'cortez',
    }
}

for names, blocks in favorite_places.items():
    set = f'{names} - модель\n\t'
    guid = f'{blocks[:]}'
    print(guid)

        