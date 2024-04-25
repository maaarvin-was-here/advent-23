with open('d19_input_test.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

i = input_lines.index('')
workflows = input_lines[:i]
parts = input_lines[i + 1:]

parsed_workflows = {}

for string in workflows:
    key = string.split('{')[0]
    rest = string.split('{')[1][:-1]
    split_rest = rest.split(',')
    final_op = split_rest.pop()
    temp = []
    for o in split_rest:
        code = o[0]
        comparator = o[1]
        o = o[2:]
        val = o.split(':')[0]
        operation = o.split(':')[1]
        temp.append([code, comparator, val, operation])
    temp.append(final_op)
    parsed_workflows[key] = temp

'''
accepted = []

for part in parts:
    part_dict = {}
    ops = part[1:-1].split(',')
    for i in ops:
        key = i.split('=')[0]
        val = int(i.split('=')[1])
        part_dict[key] = val

    cur = 'in'
    break_while = False
    while not break_while:
        current_flow = parsed_workflows[cur]
        transitioned = False
        for a in current_flow:
            if isinstance(a, str):
                if a == 'A':
                    accepted.append(part_dict)
                    break_while = True
                elif a == 'R':
                    break_while = True
                else:
                    cur = a
            else:
                if a[1] == '<':
                    if part_dict[a[0]] < int(a[2]):
                        cur = a[3]
                        if cur == 'A':
                            accepted.append(part_dict)
                            break_while = True
                        elif cur == 'R':
                            break_while = True
                        break
                elif a[1] == '>':
                    if part_dict[a[0]] > int(a[2]):
                        cur = a[3]
                        if cur == 'A':
                            accepted.append(part_dict)
                            break_while = True
                        elif cur == 'R':
                            break_while = True
                        break


sol = 0
for dict in accepted:
    sol += sum(dict.values())

print(sol)

'''

print(parsed_workflows)

def solve_workflow(l):
    s = 1
    for op in l:

        
print(solve_workflow(parsed_workflows['in']))