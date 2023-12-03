with open('d3_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

## Part 1

symbols = set()
sol = 0

# create a set of the coordinates of every symbol
for i, line in enumerate(input_lines):
    for j, char in enumerate(line):
        if not char.isnumeric() and char != '.':
            symbols.add((i, j))

valid_coords = symbols.copy()

# create a set of all coordinates adjacent to every symbol
for symbol in symbols:
    x = symbol[0]
    y = symbol[1]
    if x > 0:
        valid_coords.add((x-1, y))
        if y > 0:
            valid_coords.add((x-1, y-1))
        if y < len(input_lines[0]) - 1:
            valid_coords.add((x-1, y+1))
    if x < len(input_lines) - 1:
        valid_coords.add((x+1, y))
        if y > 0:
            valid_coords.add((x+1, y-1))
        if y < len(input_lines[0]) - 1:
            valid_coords.add((x+1, y+1))
    if y > 0:
        valid_coords.add((x, y-1))
    if y < len(input_lines[0]) - 1:
        valid_coords.add((x, y+1))


for i, line in enumerate(input_lines):
    number = 0
    y = []
    coords = []
    for j, char in enumerate(line):
        # if next character is a number, shift everything existing and add it to one's place
        if char.isnumeric():
            number *= 10
            number += int(char)
            y.append(j) # note location of digit within line

        # once number ends...
        if not char.isnumeric() or j == len(line) - 1:
            if number != 0:
                for val in y:
                    coords.append((i, val)) # note coordinate value of each number

            is_valid = False

            # use coordinates of number and adjacent coordinates of symbols to determine if value is valid
            for coord in coords:
                if coord in valid_coords:
                    is_valid = True

            if is_valid:
                sol += number

            number = 0
            y = []
            coords = []

print(sol)


## Part 2

numbers = {}
sol = 0

for i, line in enumerate(input_lines):
    number = 0
    y = []
    coords = []
    for j, char in enumerate(line):
        if char.isnumeric():
            number *= 10
            number += int(char)
            y.append(j)

        if not char.isnumeric() or j == len(line) - 1:
            if number != 0:
                for val in y:
                    coords.append((i, val))

            for coord in coords:
                numbers[coord] = (number, coords[0])

            number = 0
            y = []
            coords = []

for i, line in enumerate(input_lines):
    for j, char in enumerate(line):
        if char == '*':
            # similar code to above, find all adjacent cells to symbol
            adjacents = []
            x = i
            y = j
            if x > 0:
                adjacents.append((x - 1, y))
                if y > 0:
                    adjacents.append((x - 1, y - 1))
                if y < len(input_lines[0]) - 1:
                    adjacents.append((x - 1, y + 1))
            if x < len(input_lines) - 1:
                adjacents.append((x + 1, y))
                if y > 0:
                    adjacents.append((x + 1, y - 1))
                if y < len(input_lines[0]) - 1:
                    adjacents.append((x + 1, y + 1))
            if y > 0:
                adjacents.append((x, y - 1))
            if y < len(input_lines[0]) - 1:
                adjacents.append((x, y + 1))

            visited = []
            values = []
            for coord in adjacents:
                if coord in numbers:
                    # make sure number has not been counted before if multiple parts of number are adjacent
                    if numbers[coord][1] not in visited:
                        values.append(numbers[coord][0])
                        visited.append(numbers[coord][1])

            if len(values) == 2:
                product = values[0] * values[1]
                sol += product

print(sol)