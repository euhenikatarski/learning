d = {"name": "Евгений", "role": "QA"}

# Получает значение по ключу (без ошибки, если ключа нет)
print(d.get("role"))  # QA

# Возвращает список ключей
print(d.keys())  # dict_keys(['name', 'role'])

# Возвращает список значений
print(d.values())  # dict_values(['Евгений', 'QA'])

# Возвращает пары (ключ, значение)
print(d.items())  # dict_items([('name','Евгений'), ('role','QA')])

# Добавляет или обновляет элементы словаря
d.update({"level": "Middle"})
print(d)  # {'name':'Евгений','role':'QA','level':'Middle'}

# Удаляет элемент по ключу и возвращает его значение
print(d.pop("role"))  # QA

# Удаляет последний элемент
print(d.popitem())  # ('level', 'Middle')

# Очищает словарь
d.clear()
print(d)  # {}
