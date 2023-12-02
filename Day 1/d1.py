

with open('d1.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

sum = 0
spelled = {
    'one' : "1",
    'two' : "2",
    'three' : "3",
    'four' : "4",
    'five' : "5",
    'six' : "6",
    'seven' : "7",
    'eight' : "8",
    'nine' : "9"
}

for line in input_lines:

    for letter in line:
        if letter.isnumeric():
            first = int(letter)
    for letter in reversed(line):
        if letter.isnumeric():
            second = int(letter)
    val = (second * 10) + first
    sum += val

print(sum)


sum = 0
for line in input_lines:
    for word in spelled.keys():
        while word in line:
            index = line.index(word)
            line = line[0:index + 1] + spelled[word] + line[index + 2:]

    for letter in line:
        if letter.isnumeric():
            first = int(letter)
    for letter in reversed(line):
        if letter.isnumeric():
            second = int(letter)
    val = (second * 10) + first
    sum += val

print(sum)