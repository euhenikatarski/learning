
while True:
    x = int(input('Введите число:'))
    x = str(x)
    reversed_x = x[::-1]

    if x == reversed_x:
        print('Число палиндром')
        y = input('Пробуем еще? yes/no ')
        if y == 'no':
            break
        else:
            continue
    else:
        print('Не палиндром')
        y = input('Пробуем еще? yes/no ')
        if y == 'no':
            break
        else:
            continue

print(x)

