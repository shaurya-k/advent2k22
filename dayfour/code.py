def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total = 0
    for line in lines:
        line = line.strip()
        both = line.split(",")
        first_range = both[0]
        first_range = first_range.split("-")
        num_1 = int(first_range[0])
        num_2 = int(first_range[1])
        second_range = both[1]
        second_range = second_range.split("-")
        num_3 = int(second_range[0])
        num_4 = int(second_range[1])

        if (num_1 <= num_3 and num_2 >= num_4) or (num_3 <= num_1 and num_4 >= num_2):
            total += 1

    return total


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    total = 0
    for line in lines:
        line = line.strip()
        both = line.split(",")
        first_range = both[0]
        first_range = first_range.split("-")
        num_1 = int(first_range[0])
        num_2 = int(first_range[1])
        second_range = both[1]
        second_range = second_range.split("-")
        num_3 = int(second_range[0])
        num_4 = int(second_range[1])

        xy = range(max(num_1, num_3), min(num_2 + 1, num_4 + 1))
        if len(xy) > 0:
            total += 1

    return total


if __name__ == '__main__':
    print(one())
    print(two())
