import string

def get_alphabet_index(char):
    """
    Возвращает позицию символа в английском алфавите начиная с 1.
    :param char: символ (a-z или A-Z)
    :return: индекс символа (с 1), либо -1 если символ не найден
    """
    try:
        alphabet = list(string.ascii_lowercase)  # ['a', 'b', ..., 'z']
        char = char.lower().strip()

        if len(char) > 1:
            print(f'Вы ввели более 1 символа: --- {char} ---')
            return char
        elif len(char) < 1:
            print('Нужно ввести символ')
            return char
        elif char in alphabet:
            print(f'Буква "{char.title()}" {alphabet.index(char) + 1}-ая в алфавите')
            return alphabet.index(char) + 1
        else:
            print('Ошибка, доступны только латинские символы.')
            return char
    except AttributeError:
            print(f'Нужно ввести 1 латинский символ! Вы ввели: --- {char} ---')
            return char

char_1 = input('Введите символ: ')
result = get_alphabet_index(char_1)
