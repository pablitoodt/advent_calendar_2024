import re

def day3_part1():
    data = open("day_3/input.txt").read().strip()

    numbers = re.findall(r"mul\((\d+),(\d+)\)", data)

    total = 0
    for i in numbers:
        total += int(i[0]) * int(i[1])

    return total

print(day3_part1())
