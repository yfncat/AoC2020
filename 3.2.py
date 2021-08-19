import math

with open('3.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data]

rnd1 = 1
for n in [1, 3, 5, 7]:
    path = []
    for i in range(1, len(report)):
        path.append(report[i][(n*i) % 31])
    rnd1 = rnd1 * path.count('#')

path = []
for i in range(2, len(report)):
    path.append(report[i][(math.floor(i/2)) % 31])
    r1d2 = path[::2].count('#')

print(rnd1 * r1d2)
