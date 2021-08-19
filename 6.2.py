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

count_1 = 0
count_2 = 0
for i in range(0, len(report_2)):
    for j in string.ascii_lowercase:
        for k in range(0, len(report_2[i])):
            if j in report_2[i][k]:
                count_1 += 1
        if count_1 == len(report_2[i]):
            count_2 += 1
        count_1 = 0
print(count_2)
