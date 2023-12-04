with open('d4_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]


## Part 1

sol = 0

for line in input_lines:
    winning_numbers = []
    your_numbers = []
    num_count = 0

    numbers = line.split(': ')[1]
    win_string = numbers.split('|')[0]
    temp = win_string.split(" ")
    for val in temp:
        if val.isnumeric():
            winning_numbers.append(int(val))

    your_string = numbers.split('|')[1]
    temp = your_string.split(" ")
    for val in temp:
        if val.isnumeric():
            your_numbers.append(int(val))

    for number in your_numbers:
        if number in winning_numbers:
            num_count += 1

    if num_count == 1:
        sol += 1
    elif num_count > 1:
        points = 2**(num_count - 1)
        sol += points

print(int(sol))


## Part 2

win_map = {}
card_count = []
sol = 0

for line in input_lines:
    winning_numbers = []
    your_numbers = []
    num_count = 0
    number = 0

    cards = line.split(': ')[0]
    for char in cards:
        if char.isnumeric():
            number *= 10
            number += int(char)
    card_number = number

    numbers = line.split(': ')[1]
    win_string = numbers.split('|')[0]
    temp = win_string.split(" ")
    for val in temp:
        if val.isnumeric():
            winning_numbers.append(int(val))

    your_string = numbers.split('|')[1]
    temp = your_string.split(" ")
    for val in temp:
        if val.isnumeric():
            your_numbers.append(int(val))

    for number in your_numbers:
        if number in winning_numbers:
            num_count += 1

    win_map[card_number] = num_count
    card_count.append(1)


for i, num in enumerate(card_count):
    sol += num
    for j in range(1, win_map[num] + 1):
        if i+j < len(card_count):
            card_count[i+j] += 1

print(sol)