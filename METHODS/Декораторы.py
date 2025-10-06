# Декоратор log добавляет вывод перед вызовом функции
def log(func):
    def wrapper(*args, **kwargs):
        print("Вызов:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def test():
    return "OK"

print(test())
# Вызов: test
# OK
