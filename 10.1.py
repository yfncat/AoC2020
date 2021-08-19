with open('10.1.txt') as f:
    data = f.readlines()
    report = [int(line.strip()) for line in data]

jolt1 = 0
jolt3 = 0

prev = 0
while len(report) > 0:
    min_report = min(report)
    if min_report - prev == 1:
        jolt1 += 1
    elif min_report - prev == 3:
        jolt3 += 1
    prev = min_report
    report.remove(min_report)

print(jolt1 * (jolt3 + 1))
