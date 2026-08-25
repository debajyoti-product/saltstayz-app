import re

with open('results.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add toggle and remove headers from search widget
search_pattern = re.compile(r'(<!-- Left: Single Bar Search Widget -->\s*)<div class="flex items-center bg-\[#1a1a1a\].*?</button>\s*</div>', re.DOTALL)

new_search_widget = '''<!-- Left: Single Bar Search Widget -->
          <div class="flex flex-col gap-2 w-full xl:w-auto">
            <!-- Overnight / Day-Use Toggle -->
            <div class="flex items-center gap-1">
              <button class="bg-ss-green text-white px-4 py-1.5 text-[10px] font-bold uppercase tracking-widest transition rounded-none">Overnight</button>
              <button class="bg-gray-200 hover:bg-gray-300 text-ss-text-mute hover:text-ss-text px-4 py-1.5 text-[10px] font-bold uppercase tracking-widest transition rounded-none border border-transparent">Day-Use</button>
            </div>
            
            <div class="flex items-center bg-[#1a1a1a] p-1 shadow-lg overflow-x-auto hide-scrollbar w-full xl:w-auto">
              <!-- Location -->
              <div class="flex items-center bg-black/40 hover:bg-black/60 transition py-3 px-4 border-r border-white/10 min-w-[150px]">
                <i data-lucide="search" class="w-4 h-4 text-white/60 mr-2"></i>
                <input type="text" value="Gurgaon" class="bg-transparent border-none outline-none text-white text-[12px] font-bold w-full" />
              </div>
              <!-- Dates -->
              <div class="flex items-center justify-center bg-black/40 hover:bg-black/60 transition py-3 px-4 border-r border-white/10 min-w-[120px] cursor-pointer">
                <i data-lucide="calendar" class="w-4 h-4 text-white/60 mr-2"></i>
                <div class="text-white text-[12px] font-medium whitespace-nowrap">21 Aug - 22 Aug</div>
              </div>
              <!-- Guests -->
              <div class="flex items-center justify-center bg-black/40 hover:bg-black/60 transition py-3 px-4 border-r border-white/10 min-w-[120px] cursor-pointer">
                <i data-lucide="user" class="w-4 h-4 text-white/60 mr-2"></i>
                <div class="text-white text-[12px] font-medium whitespace-nowrap">2 GUESTS, 1 ROOM</div>
              </div>
              <!-- Book Now / Search Button -->
              <button class="bg-gradient-to-r from-ss-green to-[#6b9946] hover:from-ss-green-dark hover:to-ss-green text-white font-bold text-[12px] uppercase tracking-widest px-8 py-3 transition min-w-[120px]">
                Search
              </button>
            </div>
          </div>'''

html = search_pattern.sub(new_search_widget, html)

# 2. Remove shadow from filter widget
# Current: class="flex items-center bg-white shadow-lg rounded-none border-2 border-ss-border overflow-x-auto hide-scrollbar w-full xl:w-auto"
html = html.replace('bg-white shadow-lg rounded-none border-2 border-ss-border', 'bg-white rounded-none border-2 border-ss-border shadow-none')

# 3. Adjust spacings inside filter details popups
# Reduce p-6 to p-4, gap-6 to gap-4, gap-4 to gap-3
html = html.replace('class="p-6 overflow-y-auto"', 'class="p-4 overflow-y-auto"')
html = html.replace('class="filter-panel hidden flex-col gap-4"', 'class="filter-panel hidden flex-col gap-2.5"')
html = html.replace('class="filter-panel hidden flex-col gap-6"', 'class="filter-panel hidden flex-col gap-4"')

with open('results.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated search widget, filter shadows, and popup spacings")
