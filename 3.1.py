with open('3.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data]

path = []

for i in range(1, len(report)):
    path.append(report[i][(3*i) % 31])

print(path.count('#'))
