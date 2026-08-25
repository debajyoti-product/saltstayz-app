with open('hotel.html', 'r', encoding='utf-8') as f:
    text = f.read()
if '₹' in text:
    print('Rupee symbol is correctly encoded in the file.')
else:
    print('Rupee symbol is missing or corrupted.')
