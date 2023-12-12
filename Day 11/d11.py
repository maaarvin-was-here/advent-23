with open('d11_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

empty_rows = set()
empty_columns = set()
galaxies = set()
vertical_counts = {}

expansion_factor = 1000000

for i, line in enumerate(input_lines):
    is_empty = True
    for j, char in enumerate(line):
        if j not in vertical_counts:
            vertical_counts[j] = 0
        if char == "#":
            galaxies.add((i, j))
            vertical_counts[j] += 1
            is_empty = False
    if is_empty:
        empty_rows.add(i)

for column in vertical_counts.keys():
    if vertical_counts[column] == 0:
        empty_columns.add(column)

visited = set()


def delta_x(o, d):
    x = 0
    if o == d:
        return x
    for row in range(min(o, d), max(o, d)):
        if row in empty_rows:
            # dx += 2 (part 1)
            x += expansion_factor
        else:
            x += 1
    return x


def delta_y(o, d):
    y = 0
    if o == d:
        return y
    for col in range(min(o, d), max(o, d)):
        if col in empty_columns:
            # dy += 2 (part 1)
            y += expansion_factor
        else:
            y += 1
    return y


sum = 0

for origin in galaxies:
    visited.add(origin)
    for destination in galaxies:
        if destination not in visited:
            dx = delta_x(origin[0], destination[0])
            dy = delta_y(origin[1], destination[1])
            sum += dx + dy

print(sum)

