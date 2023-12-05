with open('d5_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]



# seeds, seed to soil, soil to fert, fert to water, water to light, light to temp, temp to hum, hum to location  - len = 8
parsed = []

temp_array = []

counter = 0

input_lines.append("")

for i in range (0, len(input_lines)):
    if len(input_lines[i]) == 0:
        counter += 1
        if temp_array:
            parsed.append(temp_array)
        temp_array = []
    else:
        x = input_lines[i].split(" ")
        if not x[0].isnumeric():
            if x[len(x) - 1].isnumeric():
                initial_seeds = input_lines[0].split(": ")[1]
                initial_seeds = [int(x) for x in initial_seeds.split(" ")]
                parsed.append(initial_seeds)
        else:
            t = [int(x) for x in input_lines[i].split(" ")]
            temp_array.append(t)


# seeds, seed to soil, soil to fert, fert to water, water to light, light to temp, temp to hum, hum to location  - len = 8

initial_seeds = parsed[0]
ranges = parsed[1:]
sol = []

for seed in initial_seeds:
    cur = seed
    for mapping in ranges:
        mapped = False
        for set in mapping:
            if not mapped:
                key = set[1]
                value = set[0]
                r = set[2]
                # print("key")
                # print(key)
                # print(value)
                # print(cur)
                if key <= cur < (key + r):
                    mapped = True
                    dif = cur - key
                    cur = value + dif

    sol.append(cur)

print(min(sol))

## Part 2

seed_ranges = initial_seeds
new_seeds = []

for i in range(0, len(seed_ranges), 2):
    for j in range(0, seed_ranges[i+1]):
        new_seeds.append(seed_ranges[i] + j)


ranges = parsed[1:]
sol = []

for seed in new_seeds:
    print(seed)
    cur = seed
    for mapping in ranges:
        mapped = False
        for set in mapping:
            if not mapped:
                key = set[1]
                value = set[0]
                range = set[2]
                # print("key")
                # print(key)
                # print(value)
                # print(cur)
                if key <= cur < (key + range):
                    mapped = True
                    dif = cur - key
                    cur = value + dif

    sol.append(cur)

print(min(sol))