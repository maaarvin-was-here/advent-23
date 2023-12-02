with open('d2.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

sum = 0

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

map = {
    "red": 0,
    "green": 1,
    "blue": 2
}

## Part 1

for line in input_lines:
    valid = True
    inputs = line.split(": ")
    game_id = int(inputs[0].split(" ")[1])

    draws = inputs[1].split("; ")

    for draw in draws:
        c = draw.split(", ")
        for combo in c:
            color = combo.split(" ")[1]
            amount = int(combo.split(" ")[0])
            if amount > limits[color]:
                valid = False

    if valid:
        sum += game_id

print(sum)

## Part 2

sum = 0
for line in input_lines:
    valid = True
    cubes = {
        "red": -1,
        "green": -1,
        "blue": -1
    }
    inputs = line.split(": ")
    game_id = int(inputs[0].split(" ")[1])

    draws = inputs[1].split("; ")

    for draw in draws:
        c = draw.split(", ")
        for combo in c:
            color = combo.split(" ")[1]
            amount = int(combo.split(" ")[0])
            if cubes[color] == -1:
                cubes[color] = amount
            else:
                cubes[color] = max(amount, cubes[color])

    vals = cubes.values()
    power = 1
    for val in vals:
        power *= val
    sum += power

print(sum)
