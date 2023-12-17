with open('d15_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

i = input_lines[0]
separated_input = i.split(",")


def hash(string):
    cur = 0
    for char in string:
        cur += ord(char)
        cur *= 17
        cur = cur % 256
    return cur


sol = 0

for string in separated_input:
    sol += hash(string)

# print(sol)

# Part 2

boxes = {}
for string in separated_input:
    if string[-1:] == '-':
        code = string.split('-')[0]
        num = hash(code)
        if num in boxes:
            for i, pair in enumerate(boxes[num]):
                if pair[0] == code:
                    boxes[num].remove(pair)
    else:
        code = string.split('=')[0]
        val = int(string.split('=')[1])
        num = hash(code)
        if num not in boxes:
            boxes[num] = []
            boxes[num].append((code, val))
        else:
            exists = False
            for i, pair in enumerate(boxes[num]):
                if pair[0] == code:
                    boxes[num][i] = (code, val)
                    exists = True
            if not exists:
                boxes[num].append((code, val))


sol2 = 0

for key in boxes:
    arr = boxes[key]
    for i, pair in enumerate(arr):
        sol2 += ((key + 1) * (i + 1) * pair[1])

print(sol2)
