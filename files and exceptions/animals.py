from pathlib import Path

file_names = ['lessons/files and exceptions/cats.txt','lessons/files and exceptions/dogs.txt','cats.txt']

for file_name in file_names:
    file_name = Path(file_name)

    try:
        content = file_name.read_text(encoding='UTF-8')
    except FileNotFoundError:
        pass
        #print(f'Такого файла нет: {file_name}')
    else:
        print(content)