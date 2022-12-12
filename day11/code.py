import math


def one():
    loop = 0
    while loop < 20:
        print(loop)
        throw(True)
        loop += 1

    overall = []
    for i in range(len(monkeys)):
        overall.append(monkeys[i]['inspected'])

    overall = sorted(overall)
    return overall[-1] * overall[-2]


def two():
    loop = 0
    divisors = []
    for i in range(len(monkeys)):
        divisors.append(monkeys[i]['test'])

    lcm = math.lcm(*divisors)

    while loop < 10000:
        print(loop)
        throw(False, lcm)
        loop += 1

    overall = []
    for i in range(len(monkeys)):
        overall.append(monkeys[i]['inspected'])

    overall = sorted(overall)
    return overall[-1] * overall[-2]


def throw(check: bool, lcm: int = 0):
    for i in range(len(monkeys)):
        curr_bananas = monkeys[i]['items']
        for j in range(len(curr_bananas)):
            banana = curr_bananas[j]

            if monkeys[i]['operation'][0] == '*':
                if monkeys[i]['operation'][1] == 'x':
                    worry_level = banana * banana
                else:
                    worry_level = banana * monkeys[i]['operation'][1]
            elif monkeys[i]['operation'][0] == '+':
                if monkeys[i]['operation'][1] == 'x':
                    worry_level = banana + banana
                else:
                    worry_level = banana + monkeys[i]['operation'][1]
            else:
                assert 1 == 2

            if check:
                worry_level = math.floor(worry_level / 3)
            else:
                worry_level = (worry_level % lcm)

            if worry_level % monkeys[i]['test'] == 0:
                monkeys[monkeys[i]['true']]['items'].append(worry_level)
            else:
                monkeys[monkeys[i]['false']]['items'].append(worry_level)
        monkeys[i]['inspected'] += len(curr_bananas)
        monkeys[i]['items'] = []


def setup():
    file = open('input.txt', 'r')
    lines = file.readlines()
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.split(' ')

        if 'Monkey' in line:
            curr_monkey = int(line[1][:-1])
            monkeys[curr_monkey] = {}
            monkeys[curr_monkey]['inspected'] = 0
        elif 'Starting' in line:
            items = []
            ind = 2
            while ind < len(line):
                if line[ind][-1] == ',':
                    items.append(int(line[ind][:-1]))
                else:
                    items.append(int(line[ind]))
                ind += 1
            monkeys[curr_monkey]['items'] = items
        elif 'Operation:' in line:
            if (line[5]) == 'old':
                monkeys[curr_monkey]['operation'] = [line[4], 'x']
            else:
                monkeys[curr_monkey]['operation'] = [line[4], int(line[5])]
        elif 'Test:' in line:
            monkeys[curr_monkey]['test'] = int(line[-1])
        elif 'true:' in line:
            monkeys[curr_monkey]['true'] = int(line[-1])
        elif 'false:' in line:
            monkeys[curr_monkey]['false'] = int(line[-1])


if __name__ == '__main__':
    monkeys = {}
    setup()
    print(one())
    setup()
    print(two())
