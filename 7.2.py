import re

with open('7.1.txt') as f:
    data = f.readlines()
    report = [line.strip() for line in data]


def bag_count(big_bag, big_bag_count, count, level):

    row = (i for i in report
           if re.findall('^.*?(?=\sbag)', i) == big_bag)

    small_bag = []
    small_bag_count = []

    for i in re.findall('\d\s.+?(?=\sbag)', next(row)):
        small_bag.append(i[2:])
        small_bag_count.append(int(i[0]))

    level *= big_bag_count

    count.append(sum(small_bag_count) * level)

    print(sum(count))

    for (j, k) in zip(small_bag, small_bag_count):
        big_bag = [j]
        big_bag_count = k

        bag_count(big_bag, big_bag_count, count, level)


bag_count(['shiny gold'], 1, [], 1)
