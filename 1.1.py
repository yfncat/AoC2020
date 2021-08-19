with open('1.1.txt') as f:
    data = f.readlines()
    report = [int(line) for line in data]

for i in report:
    j = 2020 - i
    if j in report:
        a = i * j
        print(a)
        break
