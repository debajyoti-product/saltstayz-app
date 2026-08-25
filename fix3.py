import re

with open('results.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the old Filter Bar
# It starts at <!-- Filter Bar --> and ends at the closing div of the flex row or top section
old_filter_pattern = re.compile(r'<!-- Filter Bar -->.*?</div>\s*</div>\s*</div>\s*</div>\s*<div class="max-w-\[94%\] mx-auto px-4 sm:px-6 lg:px-8 relative">', re.DOTALL)

# Let's verify the exact structure to avoid deleting too much
# In the previous edits, it was:
# <!-- Filter Bar -->
# <div class="flex items-center gap-3 overflow-x-auto hide-scrollbar">
# ...
# </div>
# </div>
# </div>
# </div>

# Let's extract the exact top container first.
match = re.search(r'(<!-- Filter Bar -->.*?)</div>\s*</div>\s*</div>\s*<div class="max-w-\[94%\]', html, re.DOTALL)
if match:
    old_filter_html = match.group(1)
    # Just remove the filter bar div entirely
    html = html.replace(old_filter_html, '')
else:
    # try looser match
    html = re.sub(r'<!-- Filter Bar -->.*?</div>\s*</div>\s*</div>\s*<div class="max-w-\[94%\]', '\n        </div>\n      </div>\n    </div>\n\n    <div class="max-w-[94%]', html, flags=re.DOTALL)

# 2. Add Floating Filter Bar & Modal HTML right before </main>
floating_bar_html = '''
    <!-- Floating Bottom Filter Bar -->
    <div class="fixed bottom-6 left-1/2 -translate-x-1/2 z-40 flex items-center bg-white shadow-2xl rounded-full border border-ss-border overflow-hidden">
      <button onclick="openFilterModal('property')" class="px-5 py-3 text-[11px] font-bold uppercase tracking-widest text-ss-text hover:bg-gray-50 transition border-r border-ss-border flex items-center gap-2 whitespace-nowrap">
        Property
      </button>
      <button onclick="openFilterModal('price')" class="px-5 py-3 text-[11px] font-bold uppercase tracking-widest text-ss-text hover:bg-gray-50 transition border-r border-ss-border flex items-center gap-2 whitespace-nowrap">
        Price
      </button>
      <button onclick="openFilterModal('locality')" class="px-5 py-3 text-[11px] font-bold uppercase tracking-widest text-ss-text hover:bg-gray-50 transition border-r border-ss-border flex items-center gap-2 whitespace-nowrap">
        Locality
      </button>
      <button onclick="openFilterModal('amenities')" class="px-5 py-3 text-[11px] font-bold uppercase tracking-widest text-ss-text hover:bg-gray-50 transition flex items-center gap-2 whitespace-nowrap">
        Amenities
      </button>
    </div>

    <!-- Filter Modals Backdrop -->
    <div id="filter-modal-backdrop" class="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm hidden items-center justify-center opacity-0 transition-opacity duration-300">
      
      <!-- Modal Container -->
      <div id="filter-modal-container" class="bg-white w-[90%] max-w-md rounded-none shadow-2xl border border-ss-border relative transform scale-95 transition-transform duration-300 flex flex-col max-h-[80vh]">
        
        <!-- Header -->
        <div class="flex items-center justify-between p-5 border-b border-ss-border">
          <h3 id="filter-modal-title" class="font-brand-display text-xl font-bold text-ss-text m-0">Filter</h3>
          <button onclick="closeFilterModal()" class="text-ss-text-mute hover:text-ss-text transition">
            <i data-lucide="x" class="w-5 h-5"></i>
          </button>
        </div>
        
        <!-- Content Panels -->
        <div class="p-6 overflow-y-auto">
          
          <!-- Property Type Panel -->
          <div id="panel-property" class="filter-panel hidden flex-col gap-4">
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Autograph (4)</span>
            </label>
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Premier (11)</span>
            </label>
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Select (9)</span>
            </label>
          </div>

          <!-- Price Panel -->
          <div id="panel-price" class="filter-panel hidden flex-col gap-6">
            <div class="flex flex-col gap-2">
              <div class="flex justify-between text-xs font-bold text-ss-text uppercase tracking-widest mb-2">
                <span>Min: ₹1000</span>
                <span id="price-max-display">Max: ₹5000</span>
              </div>
              <input type="range" min="1000" max="15000" step="500" value="5000" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-ss-green">
            </div>
            <div class="flex gap-4">
               <div class="flex-1 border border-ss-border p-3">
                 <div class="text-[9px] text-ss-text-mute uppercase tracking-widest font-bold mb-1">Minimum</div>
                 <div class="text-sm font-bold text-ss-text">₹1000</div>
               </div>
               <div class="flex-1 border border-ss-border p-3">
                 <div class="text-[9px] text-ss-text-mute uppercase tracking-widest font-bold mb-1">Maximum</div>
                 <div class="text-sm font-bold text-ss-text" id="price-max-box">₹5000</div>
               </div>
            </div>
          </div>

          <!-- Locality Panel -->
          <div id="panel-locality" class="filter-panel hidden flex-col gap-4">
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Cyber Hub</span>
            </label>
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">MG Road</span>
            </label>
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Sector 29</span>
            </label>
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Golf Course Road</span>
            </label>
          </div>

          <!-- Amenities Panel -->
          <div id="panel-amenities" class="filter-panel hidden flex-col gap-4">
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Swimming Pool</span>
            </label>
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Fitness Center</span>
            </label>
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Free Breakfast</span>
            </label>
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" class="w-5 h-5 accent-ss-green">
              <span class="text-sm font-bold text-ss-text group-hover:text-ss-green transition">Spa</span>
            </label>
          </div>
          
        </div>
        
        <!-- Footer -->
        <div class="p-5 border-t border-ss-border flex justify-between items-center bg-gray-50">
          <button onclick="closeFilterModal()" class="text-xs font-bold uppercase tracking-widest text-ss-text-mute hover:text-ss-text transition underline underline-offset-2">Clear</button>
          <button onclick="closeFilterModal()" class="bg-ss-green hover:bg-ss-green-dark text-white font-bold text-xs uppercase tracking-widest px-8 py-3 transition shadow-md rounded-none">Apply Filters</button>
        </div>
        
      </div>
    </div>
'''

html = html.replace('</main>', floating_bar_html + '\n  </main>')

# 3. Add JS for Modal
modal_js = '''
    <script>
      function openFilterModal(type) {
        const backdrop = document.getElementById('filter-modal-backdrop');
        const container = document.getElementById('filter-modal-container');
        
        document.querySelectorAll('.filter-panel').forEach(p => p.classList.add('hidden'));
        const panel = document.getElementById('panel-' + type);
        if(panel) panel.classList.remove('hidden');
        
        const titles = {
          'property': 'Property Type',
          'price': 'Price Range',
          'locality': 'Locality',
          'amenities': 'Amenities'
        };
        document.getElementById('filter-modal-title').innerText = titles[type];
        
        backdrop.classList.remove('hidden');
        backdrop.classList.add('flex');
        setTimeout(() => {
          backdrop.classList.remove('opacity-0');
          container.classList.remove('scale-95');
          container.classList.add('scale-100');
        }, 10);
      }

      function closeFilterModal() {
        const backdrop = document.getElementById('filter-modal-backdrop');
        const container = document.getElementById('filter-modal-container');
        
        backdrop.classList.add('opacity-0');
        container.classList.remove('scale-100');
        container.classList.add('scale-95');
        
        setTimeout(() => {
          backdrop.classList.add('hidden');
          backdrop.classList.remove('flex');
        }, 300);
      }
      
      document.addEventListener('DOMContentLoaded', () => {
         const backdrop = document.getElementById('filter-modal-backdrop');
         if(backdrop) {
             backdrop.addEventListener('click', (e) => {
                if (e.target === backdrop) {
                   closeFilterModal();
                }
             });
         }
         
         const priceSlider = document.querySelector('input[type="range"]');
         if(priceSlider) {
           priceSlider.addEventListener('input', (e) => {
             const val = '₹' + e.target.value;
             const display = document.getElementById('price-max-display');
             if(display) display.innerText = 'Max: ' + val;
             const box = document.getElementById('price-max-box');
             if(box) box.innerText = val;
           });
         }
      });
    </script>
'''

html = html.replace('</main>', modal_js + '\n  </main>')

with open('results.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated results.html with floating filters and modal")
