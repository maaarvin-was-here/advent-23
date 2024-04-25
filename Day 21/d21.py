with open('d21_input_test.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

grid = []

for i, line in enumerate(input_lines):
    temp = []
    for j, char in enumerate(line):
        if char == 'S':
            start = (i, j)
            temp.append('.')
        else:
            temp.append(char)
    grid.append(temp)

accessible = {}
visited = {}

q = [start]
cur_board = (0, 0)

steps = 5000
for i in range(0, steps + 1):
    print(i)
    if i not in accessible:
        accessible[i] = 0
    temp = []
    print(q)
    for coord in q:
        if cur_board not in visited:
            visited[cur_board] = set()
        # if coord not in visited[cur_board]:
        #     print("u did something wrong here")
        #     visited[cur_board].add(coord)
        #     accessible[i] += 1
        if coord not in temp:
            # iterate in all four directions
            if coord[0] - 1 >= 0:
                z = (coord[0] - 1, coord[1])
            else:
                z = (len(grid) - 1, coord[1])
                cur_board = (cur_board[0] - 1, cur_board[1])
                if cur_board not in visited:
                    visited[cur_board] = set()
            if grid[z[0]][z[1]] == '.':
                if z not in temp and z not in visited[cur_board]:
                    visited[cur_board].add(z)
                    temp.append(z)
                    accessible[i] += 1

            if coord[0] + 1 < len(grid):
                z = (coord[0] + 1, coord[1])
            else:
                z = (0, coord[1])
                cur_board = (cur_board[0] + 1, cur_board[1])
                if cur_board not in visited:
                    visited[cur_board] = set()
            if grid[z[0]][z[1]] == '.':
                if z not in temp and z not in visited[cur_board]:
                    visited[cur_board].add(z)
                    temp.append(z)
                    accessible[i] += 1

            if coord[1] + 1 < len(grid):
                z = (coord[1] + 1, coord[1])
            else:
                z = (coord[0], coord[1] + 1)
                cur_board = (cur_board[0], cur_board[1] + 1)
                if cur_board not in visited:
                    visited[cur_board] = set()
            if grid[z[0]][z[1]] == '.':
                if z not in temp and z not in visited[cur_board]:
                    visited[cur_board].add(z)
                    temp.append(z)
                    accessible[i] += 1

            if coord[1] - 1 >= 0:
                z = (coord[1] - 1, coord[1])
            else:
                z = (len(grid[0]) - 1, coord[1])
                cur_board = (cur_board[0], cur_board[1] - 1)
                if cur_board not in visited:
                    visited[cur_board] = set()
            if grid[z[0]][z[1]] == '.':
                if z not in temp and z not in visited[cur_board]:
                    visited[cur_board].add(z)
                    temp.append(z)
                    accessible[i] += 1
        # print(temp)
    q = temp

sol = 0
print(accessible)
for key in accessible:
    if key % 2 == (steps%2):
        sol += accessible[key]

print(sol)
