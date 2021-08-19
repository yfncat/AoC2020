with open('8.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data]

op = []
step = []
for i in report:
    op.append(i[0:3])
    step.append(int(i[3:]))

len_op = len(op)


def test(op, step):

    current_position = 0
    acc = 0
    ct = [0] * len_op

    while current_position < len_op:
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

    if current_position == len_op:
        return acc


current_position = 0
change_ct = [0] * len_op

while current_position < len_op:
    while change_ct[current_position] > 0:
        if op[current_position] == 'nop':
            current_position += 1
            continue
        elif op[current_position] == 'acc':
            current_position += 1
            continue
        else:
            current_position += step[current_position]
            continue

    if op[current_position] == 'nop':
        temp = op.copy()
        temp[current_position] = 'jmp'
        change_ct[current_position] += 1

        if test(temp, step) is not None:
            print(test(temp, step))
            break
    elif op[current_position] == 'acc':
        current_position += 1
        continue
    else:
        temp = op.copy()
        temp[current_position] = 'nop'
        change_ct[current_position] += 1
        if test(temp, step) is not None:
            print(test(temp, step))
            break
