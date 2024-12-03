def day2_part1():
    data = open("day_2/input.txt").read().strip()

    total = 0

    for line in data.split('\n'):
        tab = []

        for data in line.split(' '):
            tab.append(int(data))

        sup = tab[0]
        inf = tab[0]
        
        for i in range(1, len(tab)):
            if (sup != None and tab[i] > sup and tab[i] <= sup + 3):
                sup = tab[i]
            else:
                sup = None

            if (inf != None and tab[i] < inf and tab[i] >= inf - 3):
                inf = tab[i]
            else:
                inf = None

        total += 0 if sup == None else 1
        total += 0 if inf == None else 1

    return total

print(day2_part1())
