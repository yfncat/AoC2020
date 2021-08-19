with open('4.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data] + ['']

report_2 = []
passport = []
for i in range(0, len(report)):
    if not report[i] == '':
        passport.append(report[i])
    else:
        report_2.append(passport)
        passport = []

key = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
count_1 = 0
count_2 = 0
for i in range(0, len(report_2)):
    for j in key:
        if any(j in s for s in report_2[i]):
            count_1 = count_1 + 1
    if count_1 == 7:
        count_2 = count_2 + 1
    count_1 = 0

print(count_2)
