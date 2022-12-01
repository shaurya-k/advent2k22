def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    num = 0
    holder = 0
    for line in lines:
        if line != '\n':
            num += int(line)
        else:
            if num > holder:
                holder = num
            num = 0

    return holder


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    num = 0
    holder = [0, 0, 0]
    for line in lines:
        if line != '\n':
            num += int(line)
        else:
            if num > holder[0]:
                holder[0] = num
            holder.sort()
            num = 0

    return sum(holder)


if __name__ == '__main__':
    print(one())
    print(two())
