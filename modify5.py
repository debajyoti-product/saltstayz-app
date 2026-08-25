import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the h1 from Hero
hero_h1 = '''      <h1 class="font-['Jost'] text-2xl sm:text-4xl lg:text-5xl font-normal tracking-[0.12em] text-white/85 whitespace-nowrap mb-4" style="word-spacing: -0.08em;">
        <span class="font-['Caveat_Brush'] pr-1 tracking-[0.05em]">BOUTIQUE</span> <span class="text-[0.96em]">STAYS ACROSS INDIA</span>
      </h1>'''
content = content.replace(hero_h1, '')
# Also remove any leftover newlines if needed, but replace works fine.

# 2. Add it centered between Hero and Recommended
new_text_block = '''  <div class="bg-white py-12 flex justify-center items-center text-center">
    <h1 class="font-['Jost'] text-2xl sm:text-4xl lg:text-5xl font-normal tracking-[0.12em] text-ss-text whitespace-nowrap" style="word-spacing: -0.08em;">
      <span class="font-['Caveat_Brush'] pr-1 tracking-[0.05em] text-ss-green">BOUTIQUE</span> <span class="text-[0.96em]">STAYS ACROSS INDIA</span>
    </h1>
  </div>
'''

content = content.replace('<!-- Z4: Recommended For You -->', new_text_block + '\n  <!-- Z4: Recommended For You -->')

# 3. Remove the small Caveat text above Recommended
small_text = '<span class="font-[\'Caveat_Brush\'] text-2xl tracking-widest text-ss-green block mb-1">BOUTIQUE STAYS ACROSS INDIA</span>\n          '
content = content.replace(small_text, '')

# 4. Remove rounded corners from all remaining CTA cards & buttons
# Booking widget button
content = content.replace('rounded-xl hover:from-ss-green', 'rounded-none hover:from-ss-green')
# Top Nav button
content = content.replace('rounded-full hover:bg-black', 'rounded-none hover:bg-black')
# Any other CTA rounded buttons
content = content.replace('rounded-full px-3.5 py-1', 'rounded-none px-3.5 py-1') # toggle buttons in widget
content = content.replace('rounded-full px-4 py-3', 'rounded-none px-4 py-3')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
