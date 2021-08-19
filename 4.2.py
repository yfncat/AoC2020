import re

with open('4.1.txt') as f:
    data = f.readlines()
    report = []
    for i in data:
        if not i == '\n':
            i = i.split(' ')
        for j in i:
            j = j.strip()
            report.append(j)
    report = report + ['']

report_2 = {}
passport = {}
passport_count = 0
for i in report:
    if not i == '':
        passport[i[0:3]] = i[4:]
    else:
        report_2[passport_count] = passport
        passport = {}
        passport_count = passport_count + 1

ecl_key = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
passport_key = ['hgt', 'iyr', 'hcl', 'ecl', 'byr', 'eyr', 'pid']
valid_count = 0

for i in range(0, len(report_2)):
    if not all(j in report_2[i] for j in passport_key):
        continue
    # height
    elif not re.search('^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$', report_2[i]['hgt']):
        continue
    # issue yr
    elif not re.search('^20(1[0-9]|2[0-1]$)', report_2[i]['iyr']):
        continue
    # expiration yr
    elif not re.search('^20(2[0-9]|3[0-1]$)', report_2[i]['eyr']):
        continue
    # birth yr
    elif not re.search('^(19[2-9][0-9]|200[0-3])$', report_2[i]['byr']):
        continue
    # eye color
    elif not report_2[i]['ecl'] in ecl_key:
        continue
    # hair color
    elif not re.search('^#[0-9a-f]{6}$', report_2[i]['hcl']):
        continue
    # passport id
    elif not re.search('^\d{9}$', report_2[i]['pid']):
        continue
    else:
        valid_count = valid_count + 1

print(valid_count)
