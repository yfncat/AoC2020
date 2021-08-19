with open('9.1.txt') as f:
    data = f.readlines()
    report = [int(line.strip()) for line in data]

lb = 0
ub = 1
for i in report:
    report_slice = report[lb:ub]
    if sum(report_slice) == 70639851:
        print(max(report_slice)+min(report_slice))
        exit()
    elif sum(report_slice) > 70639851:
        lb += 1
    elif sum(report_slice) < 70639851:
        ub += 1
