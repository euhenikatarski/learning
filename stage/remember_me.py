from pathlib import Path
import json


def get_stored_user(path):
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None
    

def get_new_user(path):
        username = input('Введите имя: ').strip().title()
        user_secondname = input('Введите фамилию: ').strip().title()
        user = {
             'name': username,
             'second_name': user_secondname
        }
        contents = json.dumps(user)
        path.write_text(contents)
        return user


def greet_user():
    """Приветствует пользователя по имени."""
    path = Path('lessons/stage/username.json')
    user = get_stored_user(path)
    if user:
        print(f'Это вы {user['name'].title()} {user['second_name'].title()}?')
        answer = input('Y/N :')
        if answer.title() == 'N':
             user = get_new_user(path)
             print(f'Привет {user['name'].title()} {user['second_name'].title()}')
        else:
             print(f'Привет {user['name'].title()} {user['second_name'].title()}')

    else:
        user = get_new_user(path)
        print(f'Welcome {user['name'].title()} {user['second_name'].title()}, i remember u for next time')


greet_user()