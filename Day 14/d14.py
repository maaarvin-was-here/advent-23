with open('d14_input_test.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

columns = {}

for i, line in enumerate(input_lines):
    for j, char in enumerate(line):
        if char == 'O' or char == '#':
            if j not in columns:
                columns[j] = []
            columns[j].append((char, i))  # tuple (character, row)


def score():
    sol = 0

    m = len(columns.keys())

    for key in columns:
        col = columns[key]
        cur = 0
        for t in col:
            rock = t[0]
            row = t[1]
            if rock == 'O':
                sol += (m - cur)
                cur += 1
            if rock == '#':
                cur = row + 1
    return sol

# Part 1
# print(score(columns))


def switch_dimension(d):
    new = {}
    for key in d:
        for item in d[key]:
            r = item[0]
            index = item[1]

            if index not in new:
                new[index] = []
            new[index].append((r, key))

    return new


def north(d):
    for key in d:
        col = d[key]
        cur = 0
        for t in col:
            rock = t[0]
            row = t[1]
            if rock == 'O':
                sol += (m - cur)
                cur += 1
            if rock == '#':
                cur = row + 1
    return sol
def cycle(d):
    d = north(d)


