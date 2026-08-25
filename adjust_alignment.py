import re

with open('results.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change alignment of the top container so the filter bar aligns with the search bar, not the toggle
html = html.replace('class="flex flex-col xl:flex-row items-start xl:items-center justify-between gap-4"', 'class="flex flex-col xl:flex-row items-start xl:items-end justify-between gap-4"')

with open('results.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Aligned top container items to bottom")
