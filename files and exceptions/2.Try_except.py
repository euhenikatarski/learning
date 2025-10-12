while True:
    try:
        a = int(input("Введите число: "))  # пробуем преобразовать в int
        print(f"Вы ввели число: {a}")
        break  # если всё ок — выходим из цикла
    except ValueError:
        print("Ошибка: нужно ввести именно число!")
