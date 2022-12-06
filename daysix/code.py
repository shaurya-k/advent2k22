def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    buffer = []
    lines = lines[0]
    for index, val in enumerate(lines):
        if index <= 3:
            buffer.append(val)
            continue
        else:
            set_of_buffer = set(buffer)
            if len(set_of_buffer) == 4:
                return index
            else:
                buffer.pop(0)
                buffer.append(val)
    return index


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    buffer = []
    lines = lines[0]
    for index, val in enumerate(lines):
        if index <= 13:
            buffer.append(val)
            continue
        else:
            set_of_buffer = set(buffer)
            if len(set_of_buffer) == 14:
                return index
            else:
                buffer.pop(0)
                buffer.append(val)
    return index


if __name__ == '__main__':
    print(one())
    print(two())
