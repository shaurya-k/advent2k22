def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total = 1
    power = 0
    curr_cycle = 0
    for index, line in enumerate(lines):
        line = line.strip()
        if line == 'noop':
            curr_cycle += 1
            power += check(curr_cycle, total)
        else:
            curr_cycle += 1
            power += check(curr_cycle, total)
            curr_cycle += 1
            power += check(curr_cycle, total)
            total += int(line.split(" ")[1])

    return power


def check(curr_cycle, total):
    num = 0
    if curr_cycle == 20 or curr_cycle == 60 or curr_cycle == 100 or curr_cycle == 140 or curr_cycle == 180 or curr_cycle == 220:
        num = curr_cycle * total
    return num


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total = 1
    curr_cycle = 0
    image = ''
    for index, line in enumerate(lines):
        line = line.strip()
        if line == 'noop':
            image = update_image(curr_cycle, image, total)
            curr_cycle += 1
        else:
            image = update_image(curr_cycle, image, total)
            curr_cycle += 1
            image = update_image(curr_cycle, image, total)
            curr_cycle += 1
            total += int(line.split(" ")[1])
    display(image)
    return 'done'


def update_image(curr_cycle, image, place):
    if curr_cycle % 40 in [place - 1, place, place + 1]:
        image += '#'
    else:
        image += '.'
    return image


def display(image):
    for row in range(6):
        start = row * 40
        end = start + 40
        print(''.join(image[start:end]))


if __name__ == '__main__':
    print(one())
    print(two())
