while True:
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    a = input('Введите римское число: ').upper()
    total = 0
    prev = 0

    for i in reversed(a):
        value = romans.get(i, 0)
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    print("Число -", total)
    k = input('Еще раз? YES/NO: ')
    if k == 'no':
        break


