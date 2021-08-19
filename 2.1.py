with open('2.1.txt') as f:
    data = f.readlines()
    report = [line.split() for line in data]

count_range, key_char, pw = zip(*report)
key_char = ' '.join(key_char).replace(':', '').split()
count_range = ' '.join(count_range).replace('-', ' ').split()
count_range = [int(i) for i in count_range]

char_count = []
index = len(key_char)
for i in range(index):
    char_count.append(pw[i].count(key_char[i]))

count = 0
for i in range(index):
    if char_count[i] in range(count_range[2*i], count_range[2*i+1]+1):
        count = count + 1
print(count)
