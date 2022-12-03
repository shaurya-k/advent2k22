def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total = 0
    for line in lines:
        line = line.strip()

        first = line[:len(line) // 2]
        second = line[len(line) // 2:]

        common = list((set(first) & set(second)))
        common = common[0]
        if common.islower():
            total += ord(common) - 96
        else:
            total += ord(common) - 38

    return total


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total = 0
    first = ''
    second = ''
    iter = 1
    for line in lines:
        line = line.strip()

        if iter == 1:
            first = line
            iter += 1
        elif iter == 2:
            second = line
            iter += 1
        elif iter == 3:
            third = line
            a = list(set(first) & set(second) & set(third))
            a = a[0]
            if a.islower():
                total += ord(a) - 96
            else:
                total += ord(a) - 38
            iter = 1
    return total


if __name__ == '__main__':
    print(one())
    print(two())
