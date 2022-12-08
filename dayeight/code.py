def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    area = []
    for line in lines:
        line = line.strip()
        curr_row = []
        for char in line:
            curr_row.append(char)
        area.append(curr_row)

    total = 0
    for i in range(len(area)):
        for j in range(len(area[0])):
            if visible(i, j, area):
                total += 1

    return total


def visible(x, y, area):
    max_x = len(area)
    max_y = len(area[0])
    for change_x, change_y in directions:
        new_x, new_y = x + change_x, y + change_y

        while 0 <= new_x < max_x and 0 <= new_y < max_y and area[new_x][new_y] < area[x][y]:
            new_x += change_x
            new_y += change_y

        if not (0 <= new_x < max_x and 0 <= new_y < max_y):
            return True

    return False


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    area = []
    for line in lines:
        line = line.strip()
        curr_row = []
        for char in line:
            curr_row.append(char)
        area.append(curr_row)

    highest = 0
    for x in range(len(area)):
        for y in range(len(area[0])):
            found = score(x, y, area)
            if found > highest:
                highest = found

    return highest


def score(x, y, area):
    max_x = len(area)
    max_y = len(area[0])
    overall_score = 1
    for change_x, change_y in directions:
        loop_score = 0
        new_x, new_y = x + change_x, y + change_y

        while 0 <= new_x < max_x and 0 <= new_y < max_y:
            loop_score += 1
            if area[new_x][new_y] >= area[x][y]:
                break

            new_x += change_x
            new_y += change_y

        overall_score *= loop_score

    return overall_score


if __name__ == '__main__':
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    print(one())
    print(two())
