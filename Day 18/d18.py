from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

with open('d18_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

'''
directions = {
    'R' : (0, 1),
    'L' : (0, -1),
    'U' : (-1, 0),
    'D' : (1, 0)
}

# edges = []
edges = set()

cur = (0, 0)

for line in input_lines:
    dir = line.split(" ")[0]
    steps = int(line.split(" ")[1])

    for iterator in range(0, steps):
        cur_x = cur[0] + directions[dir][0]
        cur_y = cur[1] + directions[dir][1]

        cur = (cur_x, cur_y)
        # edges.append(cur)
        edges.add(cur)

num_edges = len(edges)
print(num_edges)

# Tests to see which diagonal from starting point is in the shape
# polygon = Polygon(edges)
# tp = Point(cur[0] + 1, cur[1] + 1)
# z = polygon.contains(tp)
# print(z)

# bfs
cur = (cur[0] + 1, cur[1] + 1)
queue = [cur]
visited = [cur]

sol = 0
while queue:
    coord = queue.pop(0)
    visited.append(coord)
    for key in directions:
        temp = (coord[0] + directions[key][0], coord[1] + directions[key][1])
        if temp not in edges and temp not in visited and temp not in queue:
            queue.append(temp)
    sol += 1

print(sol + num_edges)

'''

directions = {
    '0' : (0, 1),
    '2' : (0, -1),
    '3' : (-1, 0),
    '1' : (1, 0)
}

# edges = []
edges = []
cur = (0, 0)

perimeter = 0

for line in input_lines:
    t = line.split(" ")[2][2:-1]
    dir = directions[t[len(t) - 1]]
    count = 0
    code = t[0:len(t) - 1]
    for i, digit in enumerate(reversed(code)):
        if digit.isnumeric():
            count += int(digit) * (16 ** i)
        else:
            x = ord(digit) - 87
            count += x * (16 ** i)

    cur = (cur[0] + (dir[0] * count), cur[1] + (dir[1] * count))
    perimeter += count
    edges.append(cur)


def calc(a, b):
    x1, y1 = a
    x2, y2 = b
    return x1*y2-y1*x2


internal = 0
for i in range(0, len(edges)):
    p1 = edges[i]
    p2 = edges[(i+1)%len(edges)]
    internal += calc(p1, p2)

sol = abs(internal)//2 + perimeter//2 + 1
print(sol)