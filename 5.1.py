with open('5.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data]

ID = []
for i in range(0, len(report)):
    F = 0
    B = 127
    L = 0
    R = 7
    for j in report[i][:7]:
        if j == 'F':
            B = B - (B-F+1)/2
        else:
            F = F + (B-F+1)/2

    for j in report[i][7:]:
        if j == 'R':
            L = L + (R-L+1)/2
        else:
            R = R - (R-L+1)/2

    ID.append(F*8 + L)

print(max(ID))
