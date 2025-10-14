a = {1, 2, 3}
b = {3, 4, 5}

# Добавляет элемент
a.add(6)
print(a)  # {1, 2, 3, 6}

# Удаляет элемент (ошибка, если нет)
a.remove(2)
print(a)  # {1, 3, 6}

# Удаляет элемент (без ошибки, если нет)
a.discard(10)

# Объединение множеств
print(a.union(b))  # {1, 3, 4, 5, 6}

# Пересечение множеств
print(a.intersection(b))  # {3}

# Разность множеств
print(a)
print(b)
print(a.difference(b))  # {1, 6}
print(b.difference(a))  # {4, 5}
