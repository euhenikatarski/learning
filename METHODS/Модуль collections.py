from collections import Counter, defaultdict

# Counter считает количество вхождений каждого символа
cnt = Counter("qaautomation")
print(cnt)
# Counter({'a': 3, 'o': 2, 't': 2, 'q': 1, 'u': 1, 'm': 1, 'i': 1, 'n': 1})

# defaultdict задаёт значение по умолчанию для отсутствующих ключей
# Здесь int() возвращает 0, поэтому можно сразу увеличивать счётчик
d = defaultdict(int)
d["x"] += 1
print(d)
# defaultdict(<class 'int'>, {'x': 1})