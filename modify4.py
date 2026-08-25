import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('rounded-[20px]', 'rounded-none')
content = content.replace('rounded-sm', 'rounded-none')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
