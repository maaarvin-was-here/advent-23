with open('d9_input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

sol = 0

for line in input_lines:
    numbers = line.split(" ")
    numbers = [int(x) for x in numbers]
    numbers = list(reversed(numbers))

    ending = [numbers[-1]]
    array = numbers

    while array and any(x != 0 for x in array):
        temp = []
        for i in range(0, len(array) - 1):
            temp.append(array[i + 1] - array[i])
        array = temp
        ending.append(array[-1])

    sol += sum(ending)


print(sol)

'''

0
-1
0
61
514
2653
10587
35872
108738
304998
810051
2069325
5135883
12457114
1681758909

Process finished with exit code 0

'''