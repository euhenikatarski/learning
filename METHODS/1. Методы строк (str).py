s = "  Hello, QA World!  "

# Делает первую букву строки заглавной, остальные строчными
print(s.capitalize())   # "  hello, qa world!  "

# Делает все буквы заглавными
print(s.upper())        # "  HELLO, QA WORLD!  "

# Делает все буквы строчными
print(s.lower())        # "  hello, qa world!  "

# Делает первую букву каждого слова заглавной
print(s.title())        # "  Hello, Qa World!  "

# Убирает пробелы и спецсимволы по краям
print(s.strip())        # "Hello, QA World!"

# Заменяет подстроку на другую
print(s.replace("QA", "Python"))  # "  Hello, Python World!  "

# Разбивает строку по разделителю и возвращает список
print(s.split())        # ['Hello,', 'QA', 'World!']

# Объединяет список строк в одну строку через разделитель
print(",".join(["QA", "Python"])) # "QA,Python"

# Проверяет, состоит ли строка только из цифр
print("123".isdigit())  # True

# Проверяет, состоит ли строка только из букв
print("abc".isalpha())  # True
