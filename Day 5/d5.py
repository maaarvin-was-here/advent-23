with open('d5_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

# Part 1

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

'''
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
'''
## Part 2

'''
seed_ranges = initial_seeds
new_seeds = []

for i in range(0, len(seed_ranges), 2):
    new_seeds.append([(seed_ranges[i], seed_ranges[i] + seed_ranges[i+1] - 1)])

print(new_seeds)

ranges = parsed[1:]
print(ranges)

sol = []

for x in new_seeds:
    seed_range = x
    for mapping in ranges:
        new_ranges = []
        extras = []
        for subrange in seed_range:
            for set in mapping:
                start = set[1]
                val = set[0]
                r = set[2]
                end = start + r
                if start >= subrange[0] and start < subrange[1]:
                    print(start)
                    print(end)
                    print(r)
                    if end < subrange[1]:
                        print("within")
                    else:
                        print("overflow")
                        new = (subrange[0], end)
                        new_ranges.append(new)

            seed_range = new_ranges
        print(seed_range)

print(seed_range)

'''

class Function:
    def __init__(self, line):
        self.tuples: list[tuple[int,int,int]] = [x for x in line]

    def get_range(self, R):
        all = []
        for (start_value, start, duration) in self.tuples:
            end_index = start + duration
            queue = []
            while R:
                (x, y) = R.pop()
                before = (x, min(y, start))
                during = (max(x, start), min(end_index, y))
                after = (max(end_index, x), y)

                if before[1]>before[0]:
                    queue.append(before)
                if during[1]>during[0]:
                    all.append((during[0]-start+start_value, during[1]-start+start_value))
                if after[1]>after[0]:
                    queue.append(after)
            R = queue
        return all+R

sol = []

seed_ranges = initial_seeds
new_seeds = []
ranges = parsed[1:]

for i in range(0, len(seed_ranges), 2):
    new_seeds.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i+1]))

functions = [Function(x) for x in ranges]

for seed in new_seeds:
    r = [seed]

    for f in functions:
        r = f.get_range(r)
    sol.append(min(r)[0])

print(min(sol))