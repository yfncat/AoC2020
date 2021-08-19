with open('8.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data]

op = []
step = []
for i in report:
    op.append(i[0:3])
    step.append(int(i[3:]))

current_position = 0
acc = 0
ct = [0] * len(step)

while current_position < len(op):
    if ct[current_position] == 1:
        break
    else:
        if op[current_position] == 'nop':
            ct[current_position] += 1
            current_position += 1
            continue
        elif op[current_position] == 'acc':
            acc += step[current_position]
            ct[current_position] += 1
            current_position += 1
            continue
        else:
            ct[current_position] += 1
            current_position += step[current_position]

print(acc)
