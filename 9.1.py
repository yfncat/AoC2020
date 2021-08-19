with open('9.1.txt') as f:
    data = f.readlines()
    report = [int(line.strip()) for line in data]

n = 0
for i in report[n+25:]:
    report_slice = report[n:n+25]
    for j in report_slice:
        m = i - j
        if m in report_slice:
            n += 1
            break
        elif not j == report_slice[24]:
            continue
        else:
            print(i)
            exit()
