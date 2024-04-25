with open('d16_input_test.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

grid = []

for i, line in enumerate(input_lines):
    temp = []
    for j, char in enumerate(line):
        temp.append(char)
    grid.append(temp)

print(grid)

cur = (0, 0)
dir = 'R'