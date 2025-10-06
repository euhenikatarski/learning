foods = ('apple', 'grapple', 'aet', 'beef', 'strawberry')
print(foods)
for food in foods:
    print(f'{food} - есть в меню')
#foods[0] = 'milk' - в кортеж нельзя вносить изменения

print('\n-------------------------------------------------------------\n')

#Кортежу можно присвоить новое значение но нельзя изменить элементы
foods = ('apple', 'milk', 'aet', 'beef', 'strawberry')
print(foods)
for food in foods:
    print(f'{food} - есть в меню')
