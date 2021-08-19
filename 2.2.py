with open('2.1.txt') as f:
    data = f.readlines()
    report = [line.split() for line in data]

position, key_char, pw = zip(*report)
key_char = ' '.join(key_char).replace(':', '').split()
position = ' '.join(position).replace('-', ' ').split()
position = [int(i) for i in position]

count = 0
index = len(key_char)

for i in range(index):
    if pw[i][position[2 * i] - 1] == key_char[i]:
        if not pw[i][position[2 * i + 1] - 1] == key_char[i]:
            count = count + 1
    else:
        if pw[i][position[2 * i + 1] - 1] == key_char[i]:
            count = count + 1

print(count)
