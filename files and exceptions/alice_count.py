from pathlib import Path

path = Path('lessons/files and exceptions/alice.txt')
content = path.read_text(encoding='UTF-8')
content = content.lower().count('the')
print(content)

content_2 = path.read_text(encoding='UTF-8')
content_2 = content_2.lower().count('the ')
print(content_2)