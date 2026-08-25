import re

with open('hotel.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Increase Map Height
html = html.replace('h-[400px]', 'h-[460px]')

# 2. Add 'More Stays in Delhi' section right before the footer
# Let's find <!-- Z7: Footer --> and insert the section right before it.

more_stays_section = '''
    <!-- MORE STAYS IN DELHI -->
    <section class="max-w-[94%] mx-auto px-4 sm:px-6 lg:px-8 py-16 border-t border-ss-border">
      <h2 class="text-2xl font-brand-display font-bold text-ss-text mb-2">More stays in Delhi</h2>
      <p class="text-ss-text-mute text-sm mb-8 font-medium">Explore our handpicked properties with similar vibe and luxury.</p>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Compact Hotel Card 1 -->
        <a href="hotel.html" class="flex flex-col border border-ss-border bg-white shadow-sm hover:shadow-md transition group rounded-none">
          <div class="w-full h-44 overflow-hidden relative">
            <img src="https://images.unsplash.com/photo-1542314831-c6a4d27ece50?auto=format&fit=crop&w=600&q=80" alt="Saltstayz Autograph" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <div class="absolute top-3 left-3 bg-ss-green text-white text-[9px] font-bold uppercase tracking-widest px-2 py-1">20% Off</div>
          </div>
          <div class="p-5 flex flex-col gap-3">
            <div>
              <h3 class="font-brand-display text-lg font-bold text-ss-text group-hover:text-ss-green transition">Saltstayz Autograph</h3>
              <p class="text-[11px] text-ss-text-mute font-medium flex items-center gap-1 mt-1"><i data-lucide="map-pin" class="w-3 h-3 text-ss-green"></i> Cyber Hub, Delhi</p>
            </div>
            <div class="flex items-end justify-between mt-1 border-t border-ss-border pt-3">
              <div>
                <div class="text-[10px] text-ss-text-mute line-through leading-none">₹5,000</div>
                <div class="text-[17px] font-bold text-ss-green leading-none mt-1">₹4,000 <span class="text-[9px] text-ss-text-mute font-normal">/night</span></div>
              </div>
              <button class="text-[10px] font-bold uppercase tracking-widest text-ss-text border-b border-ss-text pb-0.5 group-hover:text-ss-green group-hover:border-ss-green transition">View Details</button>
            </div>
          </div>
        </a>

        <!-- Compact Hotel Card 2 -->
        <a href="hotel.html" class="flex flex-col border border-ss-border bg-white shadow-sm hover:shadow-md transition group rounded-none">
          <div class="w-full h-44 overflow-hidden relative">
            <img src="https://images.unsplash.com/photo-1596436889106-be35e843f974?auto=format&fit=crop&w=600&q=80" alt="Saltstayz Premier" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <div class="absolute top-3 left-3 bg-ss-green text-white text-[9px] font-bold uppercase tracking-widest px-2 py-1">Beyond Basic</div>
          </div>
          <div class="p-5 flex flex-col gap-3">
            <div>
              <h3 class="font-brand-display text-lg font-bold text-ss-text group-hover:text-ss-green transition">Saltstayz Premier</h3>
              <p class="text-[11px] text-ss-text-mute font-medium flex items-center gap-1 mt-1"><i data-lucide="map-pin" class="w-3 h-3 text-ss-green"></i> MG Road, Delhi</p>
            </div>
            <div class="flex items-end justify-between mt-1 border-t border-ss-border pt-3">
              <div>
                <div class="text-[10px] text-ss-text-mute line-through leading-none">₹3,500</div>
                <div class="text-[17px] font-bold text-ss-green leading-none mt-1">₹2,800 <span class="text-[9px] text-ss-text-mute font-normal">/night</span></div>
              </div>
              <button class="text-[10px] font-bold uppercase tracking-widest text-ss-text border-b border-ss-text pb-0.5 group-hover:text-ss-green group-hover:border-ss-green transition">View Details</button>
            </div>
          </div>
        </a>

        <!-- Compact Hotel Card 3 -->
        <a href="hotel.html" class="flex flex-col border border-ss-border bg-white shadow-sm hover:shadow-md transition group rounded-none">
          <div class="w-full h-44 overflow-hidden relative">
            <img src="https://images.unsplash.com/photo-1566665797739-1674de7a421a?auto=format&fit=crop&w=600&q=80" alt="Saltstayz Select" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <div class="absolute top-3 left-3 bg-ss-green text-white text-[9px] font-bold uppercase tracking-widest px-2 py-1">Early Bird</div>
          </div>
          <div class="p-5 flex flex-col gap-3">
            <div>
              <h3 class="font-brand-display text-lg font-bold text-ss-text group-hover:text-ss-green transition">Saltstayz Select</h3>
              <p class="text-[11px] text-ss-text-mute font-medium flex items-center gap-1 mt-1"><i data-lucide="map-pin" class="w-3 h-3 text-ss-green"></i> Sector 29, Delhi</p>
            </div>
            <div class="flex items-end justify-between mt-1 border-t border-ss-border pt-3">
              <div>
                <div class="text-[10px] text-ss-text-mute line-through leading-none">₹2,500</div>
                <div class="text-[17px] font-bold text-ss-green leading-none mt-1">₹1,900 <span class="text-[9px] text-ss-text-mute font-normal">/night</span></div>
              </div>
              <button class="text-[10px] font-bold uppercase tracking-widest text-ss-text border-b border-ss-text pb-0.5 group-hover:text-ss-green group-hover:border-ss-green transition">View Details</button>
            </div>
          </div>
        </a>

      </div>
    </section>

<!-- Z7: Footer -->'''

html = html.replace('<!-- Z7: Footer -->', more_stays_section)

with open('hotel.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated hotel.html")
