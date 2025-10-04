for value in range(1,21): #Выводим все числа от 1 до 20
    print(value)

print('\n-------------------------------------------------------------\n')

numbers = list(range(1,1000001))
#for number in numbers: #Выводим все числа от 1 до 1000000
#    print(f'{number}')
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print('\n-------------------------------------------------------------\n')

odd_numbers = list(range(1,20,2)) #Выводим нечетные числа от 1 до 20
print(f'{odd_numbers} - нечетные числа от 1 до 20')

print('\n-------------------------------------------------------------\n')

numbers_3 = list(range(3,31,3))  #Выводим числа кратные 3 от 3 до 30
print(f'{numbers_3} - числа кратные 3 от 3 до 30')
for number_3 in numbers_3:
    print(f'{number_3} - число кратное 3 от 3 до 30')

print('\n-------------------------------------------------------------\n')

numbers_cub = []  # Делам кубы от 1 до 10
for number_cub in range(1,11):
    numbers_cub.append(number_cub**3) #append - добавляет в список
for number_cub in  numbers_cub:
    print(f'{number_cub}')

print('\n-------------------------------------------------------------\n')

cubs = [cub**3 for cub in range(1,11)] #Генератор кубов от 1 до 10
print(cubs)
for cub in cubs:
    print(f'{cub}')