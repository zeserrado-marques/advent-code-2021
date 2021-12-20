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
scores_collection = dict()
card_count = 0
for line in fhand:
    line = line.rstrip()
    #print(line)

    # get bingo draw numbers
    if draw_numbers == None:
        draw_numbers = [int(i) for i in line.split(',')]
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
        scores_collection[f'card_{card_count+1}'] = np.zeros(current_card.shape, dtype=int)

        bingo_card.clear()
        card_count+=1

# find if drawn number is present in bingo cards
for number in draw_numbers:
    for card_key in cards_collection:
        card = cards_collection[card_key]
        for y in card:
            for x in y:
                if number == x:
                    # this is the code that finds the drawn number in the bingo card
                    result = np.where(card == x)
                    coordinate = (int(result[0]), int(result[1]))
                    # insert 1 in corresponding score card. 0 = not found. 1 = found
                    score_card = scores_collection[card_key]
                    score_card[coordinate[0], coordinate[1]] = 1
                    print(score_card)
    break

# falta fazer função em que, cada vez que um score é adicionado, ele vai verificar se há bingo feito ou não
