with open('d12_input_test.txt', 'r') as file:
    input_lines = [line.strip() for line in file]


def solve():


for line in input_lines:
    board = line.split(" ")[0]
    values = line.split(" ")[1]

    split_board = [x for x in board.split(".") if x != '']
    value_array = [int(x) for x in values.split(",")]

    print(split_board)
    print(value_array)

    for num in value_array:
