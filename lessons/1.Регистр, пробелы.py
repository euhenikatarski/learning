
name = "alex"
print(f"Здравствуй, {name.title()}, как дела?")

print('\n-------------------------------------------------------------\n')

name_2 = "aLex"
print(name.upper()) #Возводим в верхний регистр
print(name_2.lower()) #Возводим в нижний регистр

print('\n-------------------------------------------------------------\n')

famous_person = "Альберт Энштейн"
message = f"{famous_person} однажды сказал: "
print(message)

print('\n-------------------------------------------------------------\n')

name_3 = " Kri\t\nstina " #\t - таб, \n - новая строка
name_4 = name_3.strip() #обрезаем пробелы в начале и в конце
print(f'{name_3} - 3')
print(f'{name_4} - 4')

print('\n-------------------------------------------------------------\n')

filename = 'python_notes.txt'
print(filename)
filename = filename.removesuffix('.txt') #Удаляем расширение/суффикс .txt
print(filename)

print('\n-------------------------------------------------------------\n')

dog = 'https://dog.com'
print(dog)
dog = dog.removeprefix('https://') #Удаляем ссылку/префикс https://
print(dog)