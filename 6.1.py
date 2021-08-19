import string

with open('6.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data] + ['']

report_2 = []
answer = []
for i in range(0, len(report)):
    if not report[i] == '':
        answer.append(report[i])
    else:
        report_2.append(answer)
        answer = []

count = 0
for i in range(0, len(report_2)):
    for j in string.ascii_lowercase:
        if any(j in s for s in report_2[i]):
            count += 1

print(count)
