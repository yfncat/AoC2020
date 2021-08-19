with open('10.1.txt') as f:
    data = f.readlines()
    report = [int(line.strip()) for line in data]

jolt1 = 0
jolt3 = 0

prev = 0
jolt = []

while len(report) > 0:
    min_report = min(report)
    jolt.append(min_report - prev)
    prev = min_report
    report.remove(min_report)

count = 1
temp = []

jolt.append(3)

for i in jolt:
    if i == 1:
        temp.append(i)
    else:
        if len(temp) == 2:
            count *= 2
        elif len(temp) == 3:
            count *= 4
        elif len(temp) == 4:
            count *= 7

        temp.clear()

print(count)
