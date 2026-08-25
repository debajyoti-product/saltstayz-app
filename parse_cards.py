import re

with open('hotel.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Room Card 1
card1_pattern = r'(<!-- Room Card 1 -->\s*<div id="room-card-1".*?<!-- Room Card 2 -->)'
card1_match = re.search(card1_pattern, content, flags=re.DOTALL)
if not card1_match:
    print("Could not find Room Card 1")
    exit(1)

card1_html = card1_match.group(1).replace('<!-- Room Card 2 -->', '').strip()

# Create Room Card 3 from Card 1
card3_html = card1_html.replace('Room Card 1', 'Room Card 3')
card3_html = card3_html.replace('room-card-1', 'room-card-3')
card3_html = card3_html.replace('guest-overlay-1', 'guest-overlay-3')
card3_html = card3_html.replace('toggleGuestPopup(1, false)', 'toggleGuestPopup(3, false)')
card3_html = card3_html.replace('toggleGuestPopup(1, true)', 'toggleGuestPopup(3, true)')
card3_html = card3_html.replace('selectMealPlan(1, 0)', 'selectMealPlan(3, 0)')
card3_html = card3_html.replace('selectMealPlan(1, 1)', 'selectMealPlan(3, 1)')
card3_html = card3_html.replace('selectMealPlan(1, 2)', 'selectMealPlan(3, 2)')
card3_html = card3_html.replace('guest-cta-1', 'guest-cta-3')
# Change room name
card3_html = card3_html.replace('Premium room', 'Executive Suite')
card3_html = card3_html.replace(',11,500', ',14,500')
card3_html = card3_html.replace(',13,800', ',17,200')


# Extract Room Card 2
card2_pattern = r'(<!-- Room Card 2 -->\s*<div id="room-card-2".*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</section>)'
# Wait, parsing HTML with Regex can be tricky. Let's just find the exact block for card2.
# It starts with <!-- Room Card 2 --> and ends right before <!-- Amenities -->

end_pattern = r'(<!-- Room Card 2 -->.*?)(?=</section>\s*<!-- Amenities -->)'
card2_match = re.search(end_pattern, content, flags=re.DOTALL)
if not card2_match:
    print("Could not find Room Card 2 end")
    exit(1)

# card2_html is actually the rest of the room section.
# We need to split off the closing tags of the grid container.
card2_full = card2_match.group(1)

# The grid container ends with </div> just before </section>
# Let's find the last </div> in card2_full
parts = card2_full.rsplit('</div>', 1)
card2_html = parts[0] + '</div>'  # The card itself

# But wait, there is one more closing div for the grid container!
# So card2_full is: Room Card 2 HTML + </div> for grid container.
# Let's extract exactly card 2 by just using the same regex technique as Card 1, but we know it ends when the next section begins.
