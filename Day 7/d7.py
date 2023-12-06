with open('d7_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

hand_to_bid = {}

hands = []

for line in input_lines:
    hand = line.split(" ")[0]
    bet = line.split(" ")[1]
    hand_to_bid[hand] = bet
    hands.append(hand)


def sort(array):
    if len(array) == 0:
        return []
    new = []
    temp = []
    for r in ranking:
        for h in array:
            if h[0] == r:
                temp.append(h)
        if len(temp) == 1:
            new.append(temp[0])
        elif len(temp) != 0:
            prefix = temp[0][0]
            i = []
            for hand in temp:
                new_hand = hand[1:]
                i.append(new_hand)
            # AQ AK
            # A
            # [Q, K]
            # [K, Q]
            # [AK, AQ]
            i = sort(i)
            for partial in i:
                partial = prefix + partial
                new.append(partial)
        temp = []

    return new


ranking = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

# print(sort(test))

# five of a kind, four of a kind, full house, three of a kind, two pair, one pair, high card
hands_ranked = [[], [], [], [], [], [], []]

for hand in hands:
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 0
        cards[card] += 1

    card_counts = cards.values()

    max_card_count = max(card_counts)

    if max_card_count == 5:
        hands_ranked[0].append(hand)
    elif max_card_count == 4:
        hands_ranked[1].append(hand)
    elif max_card_count == 3:
        if len(card_counts) == 2:
            hands_ranked[2].append(hand)
        else:
            hands_ranked[3].append(hand)
    elif max_card_count == 2:
        if len(card_counts) == 3:
            hands_ranked[4].append(hand)
        else:
            hands_ranked[5].append(hand)
    else:
        hands_ranked[6].append(hand)

hands_sorted = []
for set in hands_ranked:
    hands_sorted.append(sort(set))

# print(hands_sorted)

counter = 0
max_rank = len(hands)

sol = 0

for s in hands_sorted:
    if len(s) > 0:
        for hand in s:
            rank = max_rank - counter
            sol += rank * int(hand_to_bid[hand])
            counter += 1

print(sol)

## Part 2

ranking = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

# AJAA3
# A5AAA

# print(sort(test))

# five of a kind, four of a kind, full house, three of a kind, two pair, one pair, high card
hands_ranked = [[], [], [], [], [], [], []]

for hand in hands:
    cards = {}
    joker_count = 0
    for card in hand:
        if card == 'J':
            joker_count += 1
        else:
            if card not in cards:
                cards[card] = 0
            cards[card] += 1

    card_counts = cards.values()

    if not card_counts:
        x = 0
    else:
        x = max(card_counts)

    max_card_count = x + joker_count

    if max_card_count == 5:
        hands_ranked[0].append(hand)
    elif max_card_count == 4:
        hands_ranked[1].append(hand)
    elif max_card_count == 3:
        if len(card_counts) == 2:
            hands_ranked[2].append(hand)
        else:
            hands_ranked[3].append(hand)
    elif max_card_count == 2:
        if len(card_counts) == 3:
            hands_ranked[4].append(hand)
        else:
            hands_ranked[5].append(hand)
    else:
        hands_ranked[6].append(hand)

hands_sorted = []
for set in hands_ranked:
    hands_sorted.append(sort(set))

# print(hands_sorted)

counter = 0
max_rank = len(hands)

sol = 0

for s in hands_sorted:
    if len(s) > 0:
        for hand in s:
            rank = max_rank - counter
            sol += rank * int(hand_to_bid[hand])
            counter += 1

print(sol)
