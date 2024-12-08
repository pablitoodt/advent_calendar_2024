import itertools

def evaluate_no_precedence(expression):
    final = int(expression[0])
    
    for i in range(1, len(expression), 2):
        operator = expression[i]
        next_value = int(expression[i + 1])
        
        if operator == "+":
            final += next_value
        elif operator == "*":
            final *= next_value
        elif operator == "||":
            final = int(str(final) + str(next_value))

    return final

def day7_part1():
    data = open("day_7/input.txt").read().strip()
    symbols = ["+", "*"]

    result = []
    total = 0

    for line in data.split('\n'):
        tab = []
        for f_number in line.split(': '):
            tab.append(f_number)

        if len(tab) > 1:
            element = tab[1].split(' ')
            tab[1] = element

        result.append(tab)

    for i in range(0, len(result)):
        combinations = list(itertools.product(symbols, repeat=len(result[i][1]) - 1))
        combinations = [list(comb) for comb in combinations]

        for combination in combinations:
            calcul_tab = []
            for number in range(0, len(combination)):
                calcul_tab.append(result[i][1][number])
                calcul_tab.append(combination[number])
            calcul_tab.append(result[i][1][-1])

            expression = evaluate_no_precedence(calcul_tab)
            if int(expression) == int(result[i][0]):
                total += int(expression)
                break

    return total

print(day7_part1())


def day7_part2():
    data = open("day_7/input.txt").read().strip()
    symbols = ["+", "*", "||"]

    result = []
    total = 0

    for line in data.split('\n'):
        tab = []
        for f_number in line.split(': '):
            tab.append(f_number)

        if len(tab) > 1:
            element = tab[1].split(' ')
            tab[1] = element

        result.append(tab)

    for i in range(0, len(result)):
        combinations = list(itertools.product(symbols, repeat=len(result[i][1]) - 1))
        combinations = [list(comb) for comb in combinations]

        for combination in combinations:
            calcul_tab = []
            for number in range(0, len(combination)):
                calcul_tab.append(result[i][1][number])
                calcul_tab.append(combination[number])
            calcul_tab.append(result[i][1][-1])

            expression = evaluate_no_precedence(calcul_tab)
            if int(expression) == int(result[i][0]):
                total += int(expression)
                break

    return total

print(day7_part2())


