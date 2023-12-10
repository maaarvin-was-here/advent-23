with open('d10_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

matrix = []

# i+ = down
# i- = up
# j+ = right
# j- = left

directions = {
    '|': ('north', 'south'),
    '-': ('east', 'west'),
    'L': ('north', 'east'),
    'J': ('north', 'west'),
    '7': ('south', 'west'),
    'F': ('south', 'east')
}

opposites = {
    'north': 'south',
    'south': 'north',
    'west': 'east',
    'east': 'west'
}

coords = {
    'north': (-1, 0),
    'south': (1, 0),
    'east': (0, 1),
    'west': (0, -1)
}


def find_start(input):
    for i, line in enumerate(input):
        temp = []
        for j, char in enumerate(line):
            temp.append(char)
            if char == 'S':
                s = i, j
        matrix.append(temp)
    return s


start = find_start(input_lines)

coord = start
cur = '|'
cur_direction = 'south'

steps = 0

pipes = set()

while cur != 'S':
    steps += 1
    pipes.add(coord)
    next_coord = (coord[0] + (coords[cur_direction][0]), coord[1] + (coords[cur_direction][1]))
    enter_next = opposites[cur_direction]
    current_type = matrix[next_coord[0]][next_coord[1]]
    if current_type == 'S':
        break
    options = directions[current_type]
    if enter_next == options[0]:
        exit_next = options[1]
    else:
        exit_next = options[0]
    coord = next_coord
    cur = current_type
    cur_direction = exit_next

print(int(steps/2))

complements = {
    '7': 'F',
    'J': 'L'
}

# ...F-7
# F--J.|
# |....|
# L----J

area = 0


for i, line in enumerate(matrix):
    cross_count = 0
    open = ''
    for j, char in enumerate(line):
        if (i, j) not in pipes and cross_count%2 != 0:
            area += 1
        elif (i, j) in pipes:
            if char == '|' or char == 'S':
                cross_count += 1
            elif char == 'F' or char == 'L':
                open = char
            elif char == '7':
                if open == 'L':
                    cross_count += 1
                else:
                    open = ''
            elif char == 'J':
                if open == 'F':
                    cross_count += 1
                else:
                    open = ''
    open = ''

print(area)