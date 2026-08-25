import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Destinations (Z5)
content = content.replace('rounded-none overflow-hidden h-60', 'rounded-none overflow-hidden h-60') # It was rounded-2xl
content = content.replace('group relative rounded-none', 'group relative rounded-none') # verify it replaced

# Collections (Z6)
content = content.replace('rounded-none p-8 flex', 'rounded-none p-8 flex') # Was rounded-3xl

# Experiences (Z7)
content = content.replace('rounded-none p-8 sm:p-12', 'rounded-none p-8 sm:p-12') # Was rounded-3xl
content = content.replace('rounded-none overflow-hidden shadow-2xl', 'rounded-none overflow-hidden shadow-2xl') # Was rounded-2xl
content = content.replace('rounded-none bg-ss-gold-dark', 'rounded-none bg-ss-gold-dark') # Was rounded-2xl in Beyond

# Testimonials (Z3)
content = content.replace('bg-white rounded-none p-6 shadow-sm', 'bg-white rounded-none p-6 shadow-sm')

# Make sure all rounded-* in these sections are rounded-none.
# We also have the header and hero which shouldn't be touched too much.

# Let's replace any ounded-full or ounded-xl in specific card classes.
content = re.sub(r'rounded-\[20px\]', 'rounded-none', content) # the price box and cta in Z4
content = re.sub(r'rounded-sm', 'rounded-none', content) # cashback tag

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
