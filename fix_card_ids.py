with open('hotel.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace within Room Card 3
start3 = content.find('<!-- Room Card 3 -->')
end3 = content.find('<!-- Room Card 4 -->')
card3 = content[start3:end3]

card3_fixed = card3.replace('updateGuests(1', 'updateGuests(3')
card3_fixed = card3_fixed.replace('adult-count-1', 'adult-count-3')
card3_fixed = card3_fixed.replace('child-count-1', 'child-count-3')
card3_fixed = card3_fixed.replace('applyGuests(1)', 'applyGuests(3)')

# Replace within Room Card 4
start4 = end3
end4 = content.find('</section>', start4)
card4 = content[start4:end4]

card4_fixed = card4.replace('updateGuests(2', 'updateGuests(4')
card4_fixed = card4_fixed.replace('adult-count-2', 'adult-count-4')
card4_fixed = card4_fixed.replace('child-count-2', 'child-count-4')
card4_fixed = card4_fixed.replace('applyGuests(2)', 'applyGuests(4)')

# Also, if Card 1 had "Selected" state (e.g. green checkmark), we might have copied it to Card 3.
# Let's check Card 3 for checkmark
if 'bg-ss-green rounded-full' in card3_fixed:
    print("Found selection mark in Card 3, removing it to match unchecked state.")
    # Card 2 is the unchecked state.
    # Let's see if we should just make Card 3 and 4 look like Card 2.
    pass

new_content = content[:start3] + card3_fixed + card4_fixed + content[end4:]

with open('hotel.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed card JS IDs.")
