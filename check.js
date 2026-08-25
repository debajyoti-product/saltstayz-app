



    tailwind.config = {
      theme: {
        extend: {
          colors: {
            'ss-green': '#4f7134',
            'ss-green-dark': '#3d5a26',
            'ss-green-soft': '#eef3e6',
            'ss-gold': '#f1e5b1',
            'ss-gold-dark': '#ffb514',
            'ss-gold-deep': '#822049',
            'ss-cream': '#f3f8ee',
            'ss-light-gold': '#f5f3ec',
            'ss-blue-dark': '#08273b',
            'ss-text': '#1a1a1a',
            'ss-text-mute': '#6a6a66',
            'ss-border': 'rgba(26, 26, 26, 0.08)',
            'ss-border-strong': 'rgba(26, 26, 26, 0.16)'
          },
          fontFamily: {
            display: ['Plus Jakarta Sans', 'Carlito', 'sans-serif'],
            body: ['Plus Jakarta Sans', 'Carlito', 'system-ui', 'sans-serif'],
          }
        }
      }
    }
  

            function toggleSeoContent() {
              const container = document.getElementById('seo-text-container');
              const fade = document.getElementById('seo-text-fade');
              const btnText = document.querySelector('#seo-view-more-btn span');
              const chevron = document.getElementById('seo-chevron');
              
              if (container.style.maxHeight === '96px') {
                container.style.maxHeight = '1500px';
                fade.style.opacity = '0';
                btnText.textContent = 'View Less';
                chevron.classList.add('rotate-180');
              } else {
                container.style.maxHeight = '96px';
                fade.style.opacity = '1';
                btnText.textContent = 'View More';
                chevron.classList.remove('rotate-180');
              }
            }
          

    lucide.createIcons();

    function setHeaderStayType(type) {
      const over = document.getElementById('tab-overnight');
      const day = document.getElementById('tab-dayuse');
      if(type === 'overnight') {
        over.className = "px-4 py-1.5 rounded-full text-xs font-bold bg-ss-green text-white shadow-sm flex items-center gap-1.5 transition";
        day.className = "px-4 py-1.5 rounded-full text-xs font-bold text-ss-text-mute hover:text-ss-green flex items-center gap-1.5 transition";
      } else {
        day.className = "px-4 py-1.5 rounded-full text-xs font-bold bg-[#822049] text-white shadow-sm flex items-center gap-1.5 transition";
        over.className = "px-4 py-1.5 rounded-full text-xs font-bold text-ss-text-mute hover:text-ss-green flex items-center gap-1.5 transition";
      }
    }

    function openSearchModal() {
      document.getElementById('search-modal').classList.remove('hidden');
      document.getElementById('search-modal').classList.add('flex');
    }
    function closeSearchModal() {
      document.getElementById('search-modal').classList.add('hidden');
      document.getElementById('search-modal').classList.remove('flex');
    }

    function toggleMobileDrawer() {
      const drawer = document.getElementById('mobile-drawer');
      drawer.classList.toggle('hidden');
    }
  

    // Beyond Interactive Logic
    const beyondToggle = document.getElementById('beyond-toggle');
    const discountRow = document.getElementById('beyond-discount-row');
    const totalValEl = document.getElementById('total-price-val');
    const beyondContainer = document.getElementById('beyond-card-container');
    
    let currentTotal = 8280;
    let targetTotal = 8280;
    
    function animatePrice() {
      if(Math.abs(targetTotal - currentTotal) > 1) {
        const diff = targetTotal - currentTotal;
        const step = Math.sign(diff) * Math.max(Math.abs(diff * 0.08), 5);
        currentTotal += step;
        totalValEl.innerText = Math.round(currentTotal).toLocaleString('en-IN');
        requestAnimationFrame(animatePrice);
      } else {
        currentTotal = targetTotal;
        totalValEl.innerText = Math.round(currentTotal).toLocaleString('en-IN');
      }
    }
    
    if(beyondToggle) {
      beyondToggle.addEventListener('change', (e) => {
        if(e.target.checked) {
          // Apply Beyond
          discountRow.style.maxHeight = '48px';
          discountRow.style.opacity = '1';
          discountRow.style.marginTop = '0px';
          beyondContainer.classList.remove('opacity-60', 'grayscale');
          targetTotal = 8280;
        } else {
          // Remove Beyond
          discountRow.style.maxHeight = '0px';
          discountRow.style.opacity = '0';
          discountRow.style.marginTop = '-12px';
          beyondContainer.classList.add('opacity-60', 'grayscale');
          targetTotal = 10080;
        }
        requestAnimationFrame(animatePrice);
      });
    }

    // Guest Selection & Room Selection Logic
    const guestState = {
      1: { adults: 1, children: 0 },
      2: { adults: 0, children: 0 },
      3: { adults: 0, children: 0 },
      4: { adults: 0, children: 0 }
    };

    function toggleGuestPopup(cardId, show) {
      const overlay = document.getElementById(`guest-overlay-${cardId}`);
      if (show) {
        overlay.classList.remove('hidden');
        overlay.classList.add('flex');
      } else {
        overlay.classList.add('hidden');
        overlay.classList.remove('flex');
      }
    }

    function updateGuests(cardId, type, delta) {
      const maxAdults = 4;
      const maxChildren = 3;
      
      let current = guestState[cardId][type];
      current += delta;
      
      if (type === 'adults') {
        if (current < 1) current = 1;
        if (current > maxAdults) current = maxAdults;
      } else {
        if (current < 0) current = 0;
        if (current > maxChildren) current = maxChildren;
      }
      
      guestState[cardId][type] = current;
      
      const countEl = document.getElementById(`${type === 'adults' ? 'adult' : 'child'}-count-${cardId}`);
      countEl.innerText = current;
    }

    function applyGuests(cardId) {
      const state = guestState[cardId];
      const btn = document.getElementById(`guest-cta-${cardId}`);
      let text = `${state.adults} Adult${state.adults > 1 ? 's' : ''}`;
      if (state.children > 0) {
        text += `, ${state.children} Child${state.children > 1 ? 'ren' : ''}`;
      }
      btn.innerText = text;
      toggleGuestPopup(cardId, false);
      updateBookingCard();
    }
    
    // Meal Plan Selection Logic
    
    // Update Booking Card Details
    function updateBookingCard() {
      const roomList = document.getElementById('booking-rooms-list');
      if (!roomList) return;
      
      // Calculate nights (static mock for now, ideally parsed from dates)
      const nights = 2;

      const allCards = [1, 2, 3, 4];
      let hasSelectedRoom = false;
      let newHtml = '';
      let subtotal = 0;

      allCards.forEach(id => {
        const card = document.getElementById(`room-card-${id}`);
        if (card && card.classList.contains('border-ss-green')) {
          hasSelectedRoom = true;
          
          // Get Room Name
          const roomTitleEl = card.querySelector('.font-brand-display');
          let roomName = 'Deluxe suite';
          if (roomTitleEl) roomName = roomTitleEl.innerText.replace(/\s*\([^)]*\)/g, '').trim(); // Strip any brackets just in case

          // Get Guest Count
          const state = guestState[id];
          const guestStr = `${state.adults} Adult${state.adults > 1 ? 's' : ''}`;

          // Get Meal Plan
          let mealPlanStr = "Room only";
          const mealCards = card.querySelectorAll('.meal-plan-card');
          mealCards.forEach(mCard => {
            if (mCard.classList.contains('border-ss-green')) {
              const mTitle = mCard.querySelector('.meal-title');
              if (mTitle) mealPlanStr = mTitle.innerText;
            }
          });

          // Get Price
          let price = id === 1 ? 5100 : 5100;
          if (mealPlanStr.includes("Breakfast & dinner")) {
            price = id === 1 ? 6800 : 7000;
          } else if (mealPlanStr.includes("Breakfast")) {
            price = id === 1 ? 5700 : 5700;
          }
          
          // Multiply by nights
          const roomTotal = price * nights;
          subtotal += roomTotal;
          
          const priceStr = "â‚¹" + roomTotal.toLocaleString('en-IN');
          
          newHtml += `
            <div class="flex justify-between items-start text-sm">
              <div>
                <div class="font-bold text-ss-text">${roomName} <span class="font-normal text-ss-text-mute">- ${nights} night${nights > 1 ? 's' : ''}</span></div>
                <div class="text-[11px] text-ss-text-mute mt-0.5">${mealPlanStr} â€¢ ${guestStr}</div>
              </div>
              <div class="font-medium text-ss-text">${priceStr}</div>
            </div>
          `;
        }
      });

      const taxesEl = document.querySelector('.text-ss-text-mute + .font-medium'); // Taxes & Fees span
      const totalPriceVal = document.getElementById('total-price-val');

      if (!hasSelectedRoom) {
        roomList.innerHTML = `<div class="text-xs text-ss-text-mute italic">No rooms selected</div>`;
        if (taxesEl && taxesEl.previousElementSibling.innerText.includes("Taxes")) taxesEl.innerText = "â‚¹0";
        if (totalPriceVal) totalPriceVal.innerText = "0";
      } else {
        roomList.innerHTML = newHtml;
        
        // Calculate taxes (mock 12% for example)
        const taxes = Math.round(subtotal * 0.12);
        if (taxesEl && taxesEl.previousElementSibling.innerText.includes("Taxes")) {
          taxesEl.innerText = "â‚¹" + taxes.toLocaleString('en-IN');
        }
        
        // Calculate total
        let total = subtotal + taxes;
        
        // Handle Beyond Discount
        const beyondToggle = document.getElementById('beyond-toggle');
        if (beyondToggle && beyondToggle.checked) {
           const discount = Math.round(total * 0.2);
           total -= discount;
           const beyondRow = document.getElementById('beyond-discount-row');
           if (beyondRow) beyondRow.querySelector('span:last-child').innerText = "- â‚¹" + discount.toLocaleString('en-IN');
        }
        
        // We set global targetTotal so requestAnimationFrame interpolates it
        if (typeof targetTotal !== 'undefined') {
          targetTotal = total;
        } else {
          if (totalPriceVal) totalPriceVal.innerText = total.toLocaleString('en-IN');
        }
        
        // Adjust sticky position if height changed
        setTimeout(adjustStickyBooking, 50);
      }
    }

    function selectMealPlan(roomIndex, planIndex) {
      const roomCard = document.getElementById(`room-card-${roomIndex}`);
      if (!roomCard) return;
      
      // If choosing a plan (0, 1, 2), prevent if room is not selected
      if (planIndex >= 0 && !roomCard.classList.contains('border-ss-green')) return;

      const mealCards = roomCard.querySelectorAll('.meal-plan-card');
      mealCards.forEach((card, idx) => {
        const titleEl = card.querySelector('.meal-title');
        const priceEl = card.querySelector('.meal-price');
        
        if (planIndex === -1) {
          // Unselected room -> unselect and dim all meal plans (including Room Only)
          card.className = "meal-plan-card rounded-none p-2 cursor-pointer transition opacity-50 pointer-events-none border border-ss-border";
          if (titleEl) titleEl.className = "meal-title text-[11px] font-normal text-ss-text mb-1 truncate";
          if (priceEl) priceEl.className = "meal-price text-[10px] text-ss-text-mute";
        } else if (idx === planIndex) {
          // Active selected meal plan
          card.className = "meal-plan-card rounded-none p-2 cursor-pointer transition opacity-100 border-2 border-ss-green bg-ss-green-soft";
          if (titleEl) titleEl.className = "meal-title text-[11px] font-bold text-ss-text mb-1 truncate";
          if (priceEl) priceEl.className = "meal-price text-[10px] text-ss-green font-bold";
        } else {
          // Unselected meal plan in an active card
          card.className = "meal-plan-card rounded-none p-2 cursor-pointer transition opacity-100 border border-ss-border hover:border-gray-300";
          if (titleEl) titleEl.className = "meal-title text-[11px] font-normal text-ss-text mb-1 truncate";
          if (priceEl) priceEl.className = "meal-price text-[10px] text-ss-text-mute";
        }
      });
    }
      setTimeout(updateBookingCard, 20);

    // Room Selection Radio/Checkbox logic
    function selectRoom(cardId) {
      const card = document.getElementById(`room-card-${cardId}`);
      if (!card) return;
      const isAlreadySelected = card.classList.contains('border-ss-green');

      const radioSvg = document.getElementById(`room-radio-${cardId}`);
      const radioBtn = document.getElementById(`room-radio-btn-${cardId}`);
      const guestCta = document.getElementById(`guest-cta-${cardId}`);
      const roomCount = document.getElementById(`room-count-${cardId}`);
      
      if (!isAlreadySelected) {
        // Select this card
        card.classList.add('border-ss-green', 'border-2');
        card.classList.remove('border-ss-border', 'border');
        
        if(radioSvg) {
          radioSvg.classList.remove('opacity-0');
          radioSvg.classList.add('opacity-100');
        }
        if(radioBtn) {
          radioBtn.classList.add('bg-ss-green', 'border-ss-green');
          radioBtn.classList.remove('bg-black/40', 'border-white/80');
        }

        // Set room count to 1
        if(roomCount) roomCount.innerText = "1";

        // Set guest CTA to 1 Adult and enable
        if(guestCta) {
          guestCta.innerText = "1 Adult";
          guestCta.disabled = false;
          guestCta.classList.remove('opacity-50', 'cursor-not-allowed', 'pointer-events-none');
          guestState[cardId] = { adults: 1, children: 0 };
        }
        
        // Select Room Only by default on selected card
        selectMealPlan(cardId, 0);
        
      } else {
        // Deselect / Uncheck this card
        card.classList.remove('border-ss-green', 'border-2');
        card.classList.add('border-ss-border', 'border');
        
        if(radioSvg) {
          radioSvg.classList.add('opacity-0');
          radioSvg.classList.remove('opacity-100');
        }
        if(radioBtn) {
          radioBtn.classList.remove('bg-ss-green', 'border-ss-green');
          radioBtn.classList.add('bg-black/40', 'border-white/80');
        }

        // Set room count to 0
        if(roomCount) roomCount.innerText = "0";

        // Set guest CTA to Select guest and disable
        if(guestCta) {
          guestCta.innerText = "Select guest";
          guestCta.disabled = true;
          guestCta.classList.add('opacity-50', 'cursor-not-allowed', 'pointer-events-none');
          guestState[cardId] = { adults: 0, children: 0 };
        }
        
        // Deselect all meal plans (including Room only) and dim them
        selectMealPlan(cardId, -1);
      }
      
      // We also need to trigger updateBookingCard if not using setTimeout in selectMealPlan,
      // but selectMealPlan already triggers updateBookingCard.
    }

    
    // Dynamic Sticky Booking Card Logic
    function adjustStickyBooking() {
      const wrapper = document.getElementById('sticky-booking-wrapper');
      if (!wrapper) return;
      
      const vh = window.innerHeight;
      const height = wrapper.offsetHeight;
      
      // If the booking card is taller than the viewport (with 100px padding), 
      // we offset the 'top' so that its bottom aligns with the viewport bottom.
      if (height > vh - 120) {
        const newTop = Math.min(vh - height - 24, 96);
        wrapper.style.top = `${newTop}px`;
      } else {
        wrapper.style.top = `96px`; // Default top-24
      }
    }
    
    window.addEventListener('scroll', adjustStickyBooking, { passive: true });
    window.addEventListener('resize', adjustStickyBooking, { passive: true });
    setTimeout(adjustStickyBooking, 100);

    
    // Day Use Logic
    let currentDayUseDuration = 3;
    let baseTimeHour = 12; // Start at 12 PM for demo

    function formatTime(hourCounter) {
        let h = hourCounter % 24;
        let suffix = h >= 12 ? 'PM' : 'AM';
        let displayH = h % 12;
        if (displayH === 0) displayH = 12;
        return `${displayH}:00 ${suffix}`;
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
            el.innerText = `${formatTime(checkinH)} - ${formatTime(checkoutH)}`;
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

            datesContainer.innerHTML = `
              <div class="col-span-2 border border-ss-border p-3 cursor-pointer hover:border-ss-green transition">
                <div class="text-[9px] font-bold text-ss-text-mute uppercase tracking-widest mb-1">Check-in</div>
                <div class="font-bold text-sm text-ss-text">Thu, 22 Aug (Day Use)</div>
              </div>`;
              
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

            datesContainer.innerHTML = `
              <div class="border border-ss-border p-3 cursor-pointer hover:border-ss-green transition">
                <div class="text-[9px] font-bold text-ss-text-mute uppercase tracking-widest mb-1">Check-in</div>
                <div class="font-bold text-sm text-ss-text">Thu, 22 Aug</div>
              </div>
              <div class="border border-ss-border p-3 cursor-pointer hover:border-ss-green transition">
                <div class="text-[9px] font-bold text-ss-text-mute uppercase tracking-widest mb-1">Check-out</div>
                <div class="font-bold text-sm text-ss-text">Sat, 24 Aug</div>
              </div>`;
        }
    }
    // Initialize default selection
    selectRoom(1);

    // Initialize Leaflet Map
    document.addEventListener("DOMContentLoaded", function() {
      if (document.getElementById('interactive-map')) {
        const map = L.map('interactive-map', {
          center: [28.632, 77.215], // Delhi
          zoom: 13,
          zoomControl: false, // Hide default zoom control to use custom buttons
          attributionControl: false // Hide default attribution to keep it clean
        });

        // Use CartoDB Voyager tiles for a clean, light aesthetic
        L.tileLayer('https://basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
          maxZoom: 19,
        }).addTo(map);

        // Bind Custom HTML Zoom Buttons
        const zoomInBtn = document.getElementById('map-zoom-in');
        const zoomOutBtn = document.getElementById('map-zoom-out');
        
        if(zoomInBtn) {
          zoomInBtn.addEventListener('click', () => map.zoomIn());
        }
        if(zoomOutBtn) {
          zoomOutBtn.addEventListener('click', () => map.zoomOut());
        }
      }
    });
  
