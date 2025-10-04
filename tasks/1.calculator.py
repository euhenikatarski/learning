while True:
    try:
        # Ввод данных
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        c = input('Выберите операцию (+, -, *, /, **): ').strip()

        # Вычисления
        if c == '+':
            result = a + b
        elif c == '*':
            result = a * b
        elif c == '-':
            result = a - b
        elif c == '/':
            if b == 0:
                print('Ошибка: Деление на ноль невозможно!')
                continue  # Начинаем заново
            result = a / b
        elif c == '**':
            result = a ** b
        else:
            print('Ошибка: Неизвестная операция! Допустимы: +, -, *, /, **')
            continue

        # Вывод результата
        print(f'Результат: {a} {c} {b} = {result}')
        break  # Выход из цикла при успешном выполнении

    except ValueError:
        print('Ошибка: Введите корректные числа!')
    except KeyboardInterrupt:
        print('\nПрограмма прервана пользователем')
        break