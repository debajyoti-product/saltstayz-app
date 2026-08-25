import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m_z3 = re.search(r'(<!-- Z3: Social Proof Strip -->.*?)(?=<!-- Z4: Recommended For You -->)', content, flags=re.DOTALL)
if m_z3:
    z3_html = m_z3.group(1)
    content = content.replace(z3_html, '')
else:
    print('Z3 not found')

m_z4 = re.search(r'(<!-- Z4: Recommended For You -->.*?)(?=<!-- Z5: Destinations Grid -->)', content, flags=re.DOTALL)
if m_z4:
    z4_html = m_z4.group(1)
    content = content.replace(z4_html, '')
else:
    print('Z4 not found')

if m_z3 and m_z4:
    # Modify Z4
    z4_html = z4_html.replace('<span class=\"text-xs font-bold uppercase tracking-widest text-ss-green\">Editor\'s Choice</span>', '<span class=\"font-[\'Caveat_Brush\'] text-2xl tracking-widest text-ss-green block mb-1\">BOUTIQUE STAYS ACROSS INDIA</span>')
    # Modify Z3
    z3_html = z3_html.replace('<span class=\"text-xs font-bold uppercase tracking-widest text-ss-green\">Verified Experiences</span>\\n          ', '')
    
    # Put Z4 then Z3
    content = content.replace('<!-- Z5: Destinations Grid -->', z4_html + z3_html + '<!-- Z5: Destinations Grid -->')

# Remove rounded corners
content = content.replace('rounded-2xl', 'rounded-none')
content = content.replace('rounded-3xl', 'rounded-none')
content = content.replace('rounded-[14px]', 'rounded-none')
content = content.replace('rounded-full shadow-sm transition shrink-0', 'rounded-none shadow-sm transition shrink-0')
content = content.replace('rounded-full hover:bg-yellow-300', 'rounded-none hover:bg-yellow-300')
content = content.replace('rounded-full hover:bg-white/10', 'rounded-none hover:bg-white/10')
content = content.replace('rounded-full border border-ss-border shadow-sm', 'rounded-none border border-ss-border shadow-sm') # the rating box in Z3

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
