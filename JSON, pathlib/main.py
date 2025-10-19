from pathlib import Path
import json

def numbers():

    path = Path('number.json')
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        
        contents_2 = path.read_text()
        number_2 = json.loads(contents_2)
        print(number_2)

    else:

        number = input(f'Введите число:')    
        contents = json.dumps(number)
        path.write_text(contents)

numbers()







