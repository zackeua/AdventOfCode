import sys

def shift_letter(letter, shift_count):
    return chr((ord(letter) - ord('a') + shift_count)%26 + ord('a'))


with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    data = [elem.strip() for elem in data]
    data = [elem[:-1].split('[') for elem in data]
    data = [[text[:text.rfind('-')], int(text[text.rfind('-')+1:]), letters] for text, letters in data]

letters = 'abcdefghijklmnopqrstuvwxyz'
for text, sector_id, checksum in data:
    text = [shift_letter(letter, sector_id) if letter != '-' else ' ' for letter in text]
    text = ''.join(text)
    letter_counts = [(text.count(letter), letter) for letter in letters]
    letter_counts.sort(key=lambda x: x[0], reverse=True)
    add_to_sum = True
    for index, letter in enumerate(checksum):
        if not letter == letter_counts[index][1]:
            add_to_sum = False
    if text == 'northpole object storage':
        print(sector_id)