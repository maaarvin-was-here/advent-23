import math

with open('d8_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

# Part 1
'''

steps = input_lines.pop(0)
input_lines.pop(0)

cells = {}

for line in input_lines:
    sbe = line.split(" = ")
    key = sbe[0]
    vals = sbe[1].split(", ")
    left = vals[0][1:]
    right = vals[1][:-1]

    cells[key] = (left, right)


def cycle(cur, sol):
    for direction in steps:
        if direction == "L":
            cur = cells[cur][0]
        elif direction == "R":
            cur = cells[cur][1]
        sol += 1
        if cur == "ZZZ":
            print("SOLVED")
            print(sol)
            return "ZZZ", sol
    return cur, sol


ended = False
sol = 0
cur = "AAA"

while cur != "ZZZ":
    cur, sol = cycle(cur, sol)

print(sol)

'''

# Part 2

steps = input_lines.pop(0)
input_lines.pop(0)

cells = {}

for line in input_lines:
    sbe = line.split(" = ")
    key = sbe[0]
    vals = sbe[1].split(", ")
    left = vals[0][1:]
    right = vals[1][:-1]

    cells[key] = (left, right)

'''
def cycle(cur, sol):
    for direction in steps:
        if direction == "L":
            for i, node in enumerate(cur):
                cur[i] = cells[node][0]
        elif direction == "R":
            for i, node in enumerate(cur):
                cur[i] = cells[node][1]
        sol += 1
        if all_z(cur):
            print("SOLVED")
            print(sol)
            return cur, sol
    print(sol)
    return cur, sol


def all_z(array):
    z = 0
    for node in array:
        if node[2] == "Z":
            z += 1
    return z == len(array)


ended = False
sol = 0
cur = []
for key in cells.keys():
    if key[2] == "A":
        cur.append(key)

while not all_z(cur):
    cur, sol = cycle(cur, sol)

print(all_z(["ZZZ", "ATZ", "33Z", "ZZZ"]))

print(sol)
'''


def cycle(cur, sol):
    for direction in steps:
        if direction == "L":
            cur = cells[cur][0]
        elif direction == "R":
            cur = cells[cur][1]
        sol += 1
        if cur[2] == "Z":
            return cur, sol
    return cur, sol


ended = False
sol_array = []
cur_array = []
for key in cells.keys():
    if key[2] == "A":
        cur_array.append(key)

for cur in cur_array:
    sol = 0
    while cur[2] != "Z":
        cur, sol = cycle(cur, sol)
    sol_array.append(sol)

# hardcoded cuz im dumb
print(sol_array)
print(math.lcm(12643, 14257, 15871, 18023, 19637, 16409))
