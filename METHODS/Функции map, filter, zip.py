nums = [1, 2, 3, 4]

# map применяет функцию к каждому элементу списка
# Здесь каждый элемент умножается на 2
print(list(map(lambda x: x*2, nums)))  # [2, 4, 6, 8]

# filter оставляет только элементы, удовлетворяющие условию
# Здесь остаются только чётные числа
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]

# zip объединяет несколько списков в пары
names = ["QA", "Dev"]
roles = ["Tester", "Developer"]
print(list(zip(names, roles)))
# [('QA', 'Tester'), ('Dev', 'Developer')]