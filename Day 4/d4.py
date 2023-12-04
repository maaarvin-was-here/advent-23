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