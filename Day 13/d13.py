import numpy as np

with open('d13_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

groups = []
temp = []
for line in input_lines:
    if len(line) == 0:
        groups.append(temp)
        temp = []
    else:
        temp.append(line)
groups.append(temp)


def all_except_one(a1, a2, size):
    dif = 0
    for i in range(0, size):
        if (i in a1 and i not in a2) or (i in a2 and i not in a1):
            dif += 1
    return dif == 1


def find_reflection(dict, opdim):
    for x in range(0, len(dict.keys())):
        if x == 0:
            prev = dict[x]
        else:
            if np.array_equal(prev, dict[x]) or all_except_one(prev, dict[x], opdim):
                mirror = True
                fixed = False
                for col in range(0, min(len(dict.keys()) - x, x)):
                    l = x - col - 1
                    r = x + col
                    if not fixed:
                        if all_except_one(dict[l], dict[r], opdim):
                            fixed = True
                        else:
                            if not np.array_equal(dict[l], dict[r]):
                                mirror = False
                    else:
                        if not np.array_equal(dict[l], dict[r]):
                            mirror = False
                if mirror and fixed:
                    return x
            else:
                prev = dict[x]

sol = 0
for group in groups:
    col_counts = {}
    row_counts = {}

    for i, row in enumerate(group):
        for j, char in enumerate(row):
            if char == '#':
                if i not in row_counts:
                    row_counts[i] = []
                row_counts[i].append(j)
                if j not in col_counts:
                    col_counts[j] = []
                col_counts[j].append(i)

    r1 = find_reflection(col_counts, len(row_counts.keys()))
    r2 = find_reflection(row_counts, len(col_counts.keys()))

    if r1 is not None:
        sol += r1
    else:
        sol += (100 * r2)

print(sol)