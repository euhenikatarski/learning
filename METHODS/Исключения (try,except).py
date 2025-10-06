try:
    x = 1 / 0  # Ошибка деления на ноль
except ZeroDivisionError as e:
    print("Ошибка:", e)  # Ошибка: division by zero