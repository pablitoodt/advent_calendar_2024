def day1_part1():
    data = open("day_1/input.txt").read().strip()

    tab1 = []
    tab2 = []
    total = 0

    for line in data.split('\n'):
        index = 0
        for data in line.split('   '):
            if (index == 0):
                tab1.append(int(data))
                index += 1
            elif (index == 1):
                tab2.append(int(data))
                index -=1
    
    tab1.sort()
    tab2.sort()

    for i in range(0, len(tab1)):
        if (tab1[i] > tab2[i]):
            total += (tab1[i] - tab2[i])
        elif (tab2[i] >= tab1[i]):
            total += (tab2[i] - tab1[i])

    return total

print(day1_part1())

def day1_part2():
    data = open("day_1/input.txt").read().strip()

    tab1 = []
    tab2 = []
    total = 0
    times = 0

    for line in data.split('\n'):
        index = 0
        for data in line.split('   '):
            if (index == 0):
                tab1.append(int(data))
                index += 1
            elif (index == 1):
                tab2.append(int(data))
                index -=1
    
    for number in tab1:
        for equal in tab2:
            if (number == equal):
                times += 1
        total += (number * times)
        times = 0
    
    return total

print(day1_part2())
