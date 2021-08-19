with open('5.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data]

seat = []
row = []
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
    row.append(F)
    seat.append([F, L])

my_row = 0
for i in range(0, 127):
    if row.count(i) == 7:
        my_row = i
    temp = []
    for j in range(0, len(seat)):
        if seat[j][0] == my_row:
            temp.append(seat[j][1])
        my_column = 0
        for k in range(0, 8):
            if k not in temp:
                my_column = k

print(my_row*8 + my_column)
