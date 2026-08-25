with open('hotel.html', 'r', encoding='utf-8') as f:
    html = f.read()

js_code = '''
    // Day Use Logic
    let currentDayUseDuration = 3;
    let baseTimeHour = 12; // Start at 12 PM for demo

    function formatTime(hourCounter) {
        let h = hourCounter % 24;
        let suffix = h >= 12 ? 'PM' : 'AM';
        let displayH = h % 12;
        if (displayH === 0) displayH = 12;
        return ${displayH}:00 ;
    }

    function updateDayUseTime() {
        const slider = document.getElementById('time-slider');
        const offset = parseInt(slider.value);
        const checkinH = baseTimeHour + offset;
        const checkoutH = checkinH + currentDayUseDuration;

        document.getElementById('checkin-time-display').innerText = formatTime(checkinH);
        
        // Update all checkout displays
        document.querySelectorAll('.duration-btn').forEach(btn => {
            const dur = parseInt(btn.querySelector('.text-sm').innerText);
            btn.querySelector('.checkout-time-text').innerText = formatTime(checkinH + dur);
        });

        // Update pills
        document.querySelectorAll('.time-pill-text').forEach(el => {
            el.innerText = ${formatTime(checkinH)} - ;
        });
    }

    function setDuration(hours, price, btnElement) {
        currentDayUseDuration = hours;
        
        // Update styling
        document.querySelectorAll('.duration-btn').forEach(btn => {
            btn.className = "duration-btn flex flex-col items-center justify-center py-3 px-2 border border-ss-border bg-white hover:border-gray-300 transition";
        });
        btnElement.className = "duration-btn flex flex-col items-center justify-center py-3 px-2 border-2 border-ss-green bg-ss-green-soft transition";

        updateDayUseTime();
    }

    function setStayType(type) {
        const btnOvernight = document.getElementById('btn-overnight');
        const btnDayuse = document.getElementById('btn-dayuse');
        const controls = document.getElementById('dayuse-controls');
        const card3 = document.getElementById('room-card-3');
        const card4 = document.getElementById('room-card-4');
        const datesContainer = document.getElementById('booking-dates-container');
        const timePills = document.querySelectorAll('.time-pill');

        if(type === 'dayuse') {
            btnDayuse.className = "px-4 py-1.5 rounded-none text-[11px] font-bold bg-gradient-to-r from-[#6b9946] to-ss-green text-white shadow-sm flex items-center gap-1.5 transition";
            btnOvernight.className = "px-4 py-1.5 rounded-none text-[11px] font-bold text-white/70 hover:text-white flex items-center gap-1.5 transition";
            
            controls.classList.remove('hidden');
            if (card3) card3.style.display = 'none';
            if (card4) card4.style.display = 'none';
            
            timePills.forEach(pill => {
                pill.classList.remove('hidden');
                pill.classList.add('flex');
            });

            datesContainer.innerHTML = 
              <div class="col-span-2 border border-ss-border p-3 cursor-pointer hover:border-ss-green transition">
                <div class="text-[9px] font-bold text-ss-text-mute uppercase tracking-widest mb-1">Check-in</div>
                <div class="font-bold text-sm text-ss-text">Thu, 22 Aug (Day Use)</div>
              </div>;
              
            // Initialize slider standard
            updateDayUseTime();

        } else {
            btnOvernight.className = "px-4 py-1.5 rounded-none text-[11px] font-bold bg-gradient-to-r from-[#6b9946] to-ss-green text-white shadow-sm flex items-center gap-1.5 transition";
            btnDayuse.className = "px-4 py-1.5 rounded-none text-[11px] font-bold text-white/70 hover:text-white flex items-center gap-1.5 transition";
            
            controls.classList.add('hidden');
            if (card3) card3.style.display = 'flex';
            if (card4) card4.style.display = 'flex';
            
            timePills.forEach(pill => {
                pill.classList.add('hidden');
                pill.classList.remove('flex');
            });

            datesContainer.innerHTML = 
              <div class="border border-ss-border p-3 cursor-pointer hover:border-ss-green transition">
                <div class="text-[9px] font-bold text-ss-text-mute uppercase tracking-widest mb-1">Check-in</div>
                <div class="font-bold text-sm text-ss-text">Thu, 22 Aug</div>
              </div>
              <div class="border border-ss-border p-3 cursor-pointer hover:border-ss-green transition">
                <div class="text-[9px] font-bold text-ss-text-mute uppercase tracking-widest mb-1">Check-out</div>
                <div class="font-bold text-sm text-ss-text">Sat, 24 Aug</div>
              </div>;
        }
    }
'''

# We inject JS at the end of the file.
html = html.replace('// Initialize default selection', js_code + '\n    // Initialize default selection')

# In the header, there was an old setStayType which we should rename or remove so it doesn't conflict.
old_func = '''    function setStayType(type) {
      const over = document.getElementById('tab-overnight');
      const day = document.getElementById('tab-dayuse');'''

new_func = '''    function setHeaderStayType(type) {
      const over = document.getElementById('tab-overnight');
      const day = document.getElementById('tab-dayuse');'''

html = html.replace(old_func, new_func)
html = html.replace('onclick="setStayType(', 'onclick="setHeaderStayType(') # Wait, this might replace our newly added ones!
# Let's fix that. I'll replace it globally, then fix the ones in the new toggle.
html = html.replace('onclick="setHeaderStayType(\'overnight\')" id="btn-overnight"', 'onclick="setStayType(\'overnight\')" id="btn-overnight"')
html = html.replace('onclick="setHeaderStayType(\'dayuse\')" id="btn-dayuse"', 'onclick="setStayType(\'dayuse\')" id="btn-dayuse"')

with open('hotel.html', 'w', encoding='utf-8') as f:
    f.write(html)
