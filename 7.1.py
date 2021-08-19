import re

with open('7.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data]


def bag_count(report, small_bag, prev_count, curr_count):
    if prev_count == curr_count:
        return print(curr_count)
    else:
        prev_count = curr_count
        for i in range(0, len(report)):
            for j in small_bag:
                if j in re.findall('(?<=\d\s).+?(?=\sbag)', report[i]):
                    small_bag += re.findall('^.*?(?=\sbag)', report[i])

        small_bag = list(dict.fromkeys(small_bag))
        curr_count = len(small_bag) - 1
        bag_count(report, small_bag, prev_count, curr_count)


small_bag = ['shiny gold']

bag_count(report, small_bag, 0, 1)
