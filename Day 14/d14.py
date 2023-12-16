import operator
from collections import deque
import regex as re

with open('d14_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

columns = {}
width, height = len(input_lines[0]), len(input_lines)

for i, line in enumerate(input_lines):
    for j, char in enumerate(line):
        if char == 'O' or char == '#':
            if j not in columns:
                columns[j] = []
            columns[j].append((char, i))  # tuple (character, row)


def p1():
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


def switch_dimension(d):
    new = {}
    for key in d:
        for item in d[key]:
            r = item[0]
            index = item[1]

            if index not in new:
                new[index] = []
            new[index].append((r, key))

    for key in new:
        new[key].sort(key=operator.itemgetter(1))

    return new


def score(d):
    sol = 0
    m = len(d.keys())

    d = switch_dimension(d)

    for key in d:
        row = d[key]
        count = 0
        for t in row:
            rock = t[0]
            if rock == 'O':
                count += 1
        sol += ((m - key) * count)

    return sol


# Part 1
# print(p1())


def north(d):
    for key in d:
        new = []
        col = d[key]
        cur = 0
        for t in col:
            rock = t[0]
            row = t[1]
            if rock == 'O':
                new.append(('O', cur))
                cur += 1
            if rock == '#':
                new.append(('#', row))
                cur = row + 1
        d[key] = new
    return d


def south_or_east(d, dir):
    for key in d:
        new = []
        new = deque(new)
        col = d[key]
        if dir == 'east':
            cur = width - 1
        elif dir == 'south':
            cur = height - 1
        else:
            print("ERROR")
            return {}
        for t in reversed(col):
            rock = t[0]
            row = t[1]
            if rock == 'O':
                new.appendleft(('O', cur))
                cur -= 1
            if rock == '#':
                new.appendleft(('#', row))
                cur = row - 1
        new = list(new)

        d[key] = new
    return d


def cycle(d):
    d = north(d)  # north
    d = switch_dimension(d)
    d = north(d)  # west
    d = switch_dimension(d)
    d = south_or_east(d, 'south')
    d = switch_dimension(d)
    d = south_or_east(d, 'east')
    d = switch_dimension(d)
    return d


seen = []

for i in range(0, 1000000000):
    columns = cycle(columns)
    l = [columns[x] for x in sorted(columns.keys())]
    if l in seen:
        cycle_length = i - seen.index(l)
        cycle_start = seen.index(l)
        break
    seen.append(l)

extra_cycles = (1000000000 - cycle_start)%cycle_length

for i in range(0, extra_cycles - 1):
    columns = cycle(columns)

print(score(columns))
