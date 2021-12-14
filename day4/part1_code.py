'''
--- Day 4: Giant Squid ---

Let's create a bingo game

'''
import numpy as np


#fhand = open('input.txt')
fhand = open('test.txt')

# load data
draw_numbers = None
bingo_card = []

cards_collection = dict()
card_count = 0
for line in fhand:
    line = line.rstrip()
    print(line)

    # get bingo draw numbers
    if draw_numbers == None:
        draw_numbers = line
        continue
    
    # skip empty lines
    if len(line) == 0:
        continue

    # get bingo cards
    line_bingo = [int(i) for i in line.split()]
    bingo_card.append(line_bingo)

    if len(bingo_card) == 5:
        current_card = np.asarray_chkfinite(bingo_card)
        cards_collection[f'card_{card_count+1}'] = current_card

        bingo_card.clear()
        card_count+=1

for key in cards_collection:
    print(key, cards_collection[key], sep='\n')
