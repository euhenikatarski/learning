while True:
    try:
        a = float(input('Введите первое число:'))
        b = float(input('Введите второе число:'))
        c = input('Введите операцию +, -, *, /, **, %: ').strip()
    
        if c == '+':
            result = a + b

        elif c == '*':
            result = a * b

        elif c == '/':
            result = a / b
            
        elif c == '-':
            result = a - b
            
        elif c == '**':
            result = a ** b
        
        elif c == '%':
            result = a % b

        else:
            print('Ошибка')
            continue
    
        print(f'Результат: {a} {c} {b} = {result}')
        continue

    except ValueError:
        print('Нужно ввести числа')

    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    
    except KeyboardInterrupt:
        print('\nПользователь прервал программу')
        break