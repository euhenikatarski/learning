alien_color = 'red'
if alien_color == 'green':
    print('Вы заработали 5 очков')
if alien_color == "red":
    print('Вы заработали 100 очков')

print('\n-------------------------------------------------------------\n')

if alien_color == 'green':
    print('Вы заработали 5 очков')
if alien_color != "green":
    print('Вы заработали 15 очков')

print('\n-------------------------------------------------------------\n')

if alien_color == 'green':
    print('Вы заработали 5 очков')
else:
    print('Вы заработали 20 очков')

print('\n-------------------------------------------------------------\n')

if alien_color == 'green':
    score = 12
elif alien_color == 'yellow':
    score = 15
elif alien_color == 'red':
    score = 19
print(f'Ты получил {score} очков')

print('\n-------------------------------------------------------------\n')

age = 87
if  age < 2:
    life_period = 'Младенец'
elif age >= 2 and age < 13:
    life_period = 'Ребенок'
elif age >= 13 and age < 20:
    life_period = 'Подросток'
elif age >= 20 and age < 65:
    life_period = 'Взрослый'
else:
    life_period = 'Пожилой'
print(f'{life_period}')

print('\n-------------------------------------------------------------\n')

favorite_fruits = ['apple','orange','pineapple','banana']
if 'apple' in favorite_fruits:
    print('Яблоки любим')
if 'sandwich' in favorite_fruits:
    print('sandwich')
if 'banana' in favorite_fruits:
    print('Banana')