pizzas = ['pepperoni','margarita','fourseasons','boloneza']
print(f'\n{pizzas[:2]}')  #С начала списка до нужного индекса
print(f'\n{pizzas[1:3]}')  #Середина спика
print(f'\n{pizzas[1:]}')  #С середины до конца списка

print('\n-------------------------------------------------------------\n')

my_pizzas = ['pepperoni','margarita','fourseasons','boloneza']
friend_pizzas = my_pizzas[:]  #Копируем список, списки идентичны и не зависимы
print(my_pizzas)
print(friend_pizzas)
my_pizzas.append('joulen')   #Добавляем в свой список пиццу и проверяем что ее нет в списке друга
friend_pizzas.append('kuretta')   #Добавляем в список друга пиццу и проверяем что ее нет в нашем списке
print(my_pizzas)
print(friend_pizzas)

print('\n-------------------------------------------------------------\n')

for my_pizza in my_pizzas:
    print(f'\n{my_pizza.title()} - одна из моих любимых пицц')  #Выводим список своих пицц
for friend_pizza in friend_pizzas:
    print(f'\n{friend_pizza.title()} - одна из любимых пицц моего друга')  #Выводим список пицц друга

print('\n-------------------------------------------------------------\n')
