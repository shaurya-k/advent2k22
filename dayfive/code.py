def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    one = ['p', 'd', 'q', 'r', 'v', 'b', 'h', 'f']
    two = ['v', 'w', 'q', 'z', 'd', 'l']
    three = ['c', 'p', 'r', 'g', 'q', 'z', 'l', 'h']
    four = ['b', 'v', 'j', 'f', 'h', 'd', 'r']
    five = ['c', 'l', 'w', 'z']
    six = ['m', 'v', 'g', 't', 'n', 'p', 'r', 'j']
    seven = ['s', 'b', 'm', 'v', 'l', 'r', 'j']
    eight = ['j', 'p', 'd']
    nine = ['v', 'w', 'n', 'c', 'd']
    lists = ['', one, two, three, four, five, six, seven, eight, nine]
    for index, line in enumerate(lines):
        if index <= 9:
            continue
        line = line.strip()
        both = line.split(" ")
        num = int(both[1])
        start = int(both[3])
        end = int(both[5])

        a = 0
        while a < num:
            lists[end].insert(0, lists[start].pop(0))
            a += 1

    ans = ''
    for ind in lists:
        if len(ind) > 0:
            ans += ind[0]

    return ans.upper()


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    one = ['p', 'd', 'q', 'r', 'v', 'b', 'h', 'f']
    two = ['v', 'w', 'q', 'z', 'd', 'l']
    three = ['c', 'p', 'r', 'g', 'q', 'z', 'l', 'h']
    four = ['b', 'v', 'j', 'f', 'h', 'd', 'r']
    five = ['c', 'l', 'w', 'z']
    six = ['m', 'v', 'g', 't', 'n', 'p', 'r', 'j']
    seven = ['s', 'b', 'm', 'v', 'l', 'r', 'j']
    eight = ['j', 'p', 'd']
    nine = ['v', 'w', 'n', 'c', 'd']
    lists = ['', one, two, three, four, five, six, seven, eight, nine]
    for index, line in enumerate(lines):
        if index <= 9:
            continue
        line = line.strip()
        both = line.split(" ")
        num = int(both[1])
        start = int(both[3])
        end = int(both[5])

        remove = lists[start][:num]  # crates being moved
        lists[start] = lists[start][num:]  # crates that stay
        remove.extend(lists[end])  # adding crates to new box
        lists[end] = remove  # reassign

    ans = ''
    for ind in lists:
        if len(ind) > 0:
            ans += ind[0]

    return ans.upper()


if __name__ == '__main__':
    print(one())
    print(two())
