import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<span class=\"text-xs font-bold uppercase tracking-widest text-ss-green\">\s*Verified Experiences\s*</span>', '', content)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
