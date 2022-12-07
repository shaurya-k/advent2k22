def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    pwd = ''
    space = {}
    for line in lines:
        line = line.strip()
        if '$' in line:
            if 'cd ..' in line:
                if pwd == 'root':
                    continue
                else:
                    pwd = pwd[:pwd.rfind('/')]
            elif 'cd' in line:
                folder = line.split(' ')[2]
                if folder == '/':
                    pwd = 'root'
                else:
                    pwd += f'/{folder}'
                space[pwd] = 0
            elif 'ls' in line:
                pass

        else:
            if 'dir' in line:
                pass
            else:
                temp = pwd
                size = int(line.split(' ')[0])
                while temp:
                    space[temp] += size
                    if '/' in temp:
                        temp = temp[:temp.rindex('/')]
                    else:
                        break

    sum = 0
    for value in space.values():
        if value <= 100000:
            sum += value
    return sum


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    pwd = ''
    space = {}
    for line in lines:
        line = line.strip()
        if '$' in line:
            if 'cd ..' in line:
                if pwd == 'root':
                    continue
                else:
                    pwd = pwd[:pwd.rfind('/')]
            elif 'cd' in line:
                folder = line.split(' ')[2]
                if folder == '/':
                    pwd = 'root'
                else:
                    pwd += f'/{folder}'
                space[pwd] = 0
            elif 'ls' in line:
                pass

        else:
            if 'dir' in line:
                pass
            else:
                temp = pwd
                size = int(line.split(' ')[0])
                while temp:
                    space[temp] += size
                    if '/' in temp:
                        temp = temp[:temp.rindex('/')]
                    else:
                        break

    total_used = space['root']
    to_free = total_used + 30000000 - 70000000
    to_delete = 70000000 
    for v in space.values():
        if to_free < v < to_delete:
            to_delete = v
    return to_delete


if __name__ == '__main__':
    print(one())
    print(two())
