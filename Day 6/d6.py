with open('d6_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]


## Part 1

t = input_lines[0].split(": ")[1]
t = t.split(" ")
time = []
for num in t:
    if num.isnumeric():
        time.append(int(num))

d = input_lines[1].split(": ")[1]
d = d.split(" ")
distance = []
for num in d:
    if num.isnumeric():
        distance.append(int(num))

sol = []

for i in range(0, len(time)):
    t = time[i]
    d = distance[i]
    win_count = 0
    for j in range(0, t):
        if j * (t - j) > d:
            win_count += 1
    sol.append(win_count)

ans = 1
for s in sol:
    ans *= s
print(ans)

# time_elapsed * t - time_elapsed > distance

## Part 2

t = input_lines[0].split(": ")[1]
t = t.split(" ")
time = ""
for num in t:
    if num.isnumeric():
        time += num

time = int(time)

d = input_lines[1].split(": ")[1]
d = d.split(" ")
distance = ""
for num in d:
    if num.isnumeric():
        distance += num

distance = int(distance)


t = time
d = distance
win_count = 0
for j in range(0, t):
    if j * (t - j) > d:
        win_count += 1

print(win_count)