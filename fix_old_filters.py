import re

with open('results.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The old filter bar starts with <!-- Right: Filter Bar -->
# and ends right before </div>\n        </div>\n      </div>\n    </div>\n\n    <div class="max-w-[94%] mx-auto

pattern = re.compile(r'<!-- Right: Filter Bar -->.*?</div>\s*</div>\s*</div>\s*<div class="max-w-\[94%\] mx-auto px-4 sm:px-6 lg:px-8 relative">', re.DOTALL)
html = pattern.sub(r'</div>\n      </div>\n    </div>\n\n    <div class="max-w-[94%] mx-auto px-4 sm:px-6 lg:px-8 relative">', html)

with open('results.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Old filter bar removed successfully")
