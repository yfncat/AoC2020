with open('1.1.txt') as f:
    data = f.readlines()
    report = [int(line) for line in data]

report_2 = []
for i in report:
    report_2.append(2020 - i)

for x in report_2:
    for y in report:
        z = x - y
        if z in report:
            if not z == y:
                break
    else:
        continue
    break

print(z * y * report[report_2.index(x)])
