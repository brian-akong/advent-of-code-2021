from input_data import numbers, raw_bingo_card_data
import itertools

bingo_cards = []
singular_bingo_card = []
row = []

print(f'numbers = {len(numbers)}')

# create bingo cards
for index, num in enumerate(raw_bingo_card_data):
    if index == len(raw_bingo_card_data) - 1:
        singular_bingo_card.append(row)
        bingo_cards.append(singular_bingo_card)
    if index > 0 and index % 5 == 0:
        singular_bingo_card.append(row)
        row = []
        if index % 25 == 0:
            bingo_cards.append(singular_bingo_card)
            singular_bingo_card = []
    row.append(num)

def winning_card(bingo_card, called_numbers):
    # check all rows
    counter = 0
    for row_index, row in enumerate(bingo_card):
        if counter == 5:
            return True
        counter = 0
        for element_index, element in enumerate(row):
            if bingo_card[row_index][element_index] not in called_numbers:
                ret = False
            else:
                counter += 1

    # check all columns
    for column_index, column in enumerate(bingo_card):
        if counter == 5:
            return True
        counter = 0
        for i in range(5):
            if bingo_card[i][column_index] not in called_numbers:
                ret = False
            else:
                counter += 1
    return ret

called_numbers = []

for number in numbers:
    called_numbers.append(number)
    for card in bingo_cards:
        if winning_card(card, called_numbers) == True:
            print(f'called_numbers = {called_numbers}')
            print(f'card = {card}')
            unmarked_numbers = [x for x in itertools.chain(*card) if x not in called_numbers]
            print(f'unmarked_numbers = {unmarked_numbers}')
            print(f'final answer - {called_numbers[-1]} x {sum(unmarked_numbers)}: {called_numbers[-1] * sum(unmarked_numbers)}')
            break
    if winning_card(card, called_numbers) == True:
            break

##### Part 2
# Remove winning bingo cards until 1 remains
called_numbers = []
for number in numbers:
    if len(bingo_cards) == 1:
        break
    called_numbers.append(number)
    for card in bingo_cards:
        if winning_card(card, called_numbers) == True:
            bingo_cards.remove(card)

print(f'called_numbers = {called_numbers}')
print(f'final card = {bingo_cards[0]}')
unmarked_numbers = [x for x in itertools.chain(*bingo_cards[0]) if x not in called_numbers]
print(f'unmarked_numbers = {unmarked_numbers}')
print(f'PART 2 final answer - {called_numbers[-1]} x {sum(unmarked_numbers)}: {called_numbers[-1] * sum(unmarked_numbers)}')