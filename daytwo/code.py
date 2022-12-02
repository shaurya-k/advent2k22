def one():
    file = open('input.txt', 'r')
    lines = file.readlines()
    letters = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}  # map scores
    change = {"X": "A", "Y": "B", "Z": "C"}  # transform to match mine to opp

    val = 0
    for line in lines:
        opp = line[0]
        mine = line[2]
        mine = change[mine]

        if mine == opp:  # draw
            val += 3
            val += letters[mine]

        elif mine == "A" and opp == "C":  # rock v scissors win
            val += 6
            val += letters[mine]

        elif mine == "B" and opp == "A":  # paper v rock win
            val += 6
            val += letters[mine]

        elif mine == "C" and opp == "B":  # scissors v rock win
            val += 6
            val += letters[mine]

        else:  # lose
            val += letters[mine]
    return val


def two():
    file = open('input.txt', 'r')
    lines = file.readlines()
    letters = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}

    val = 0
    lose = {"A": "C", "B": "A", "C": "B"}
    win = {"A": "B", "B": "C", "C": "A"}
    for line in lines:
        opp = line[0]
        me = line[2]

        if me == "Y":  # tie
            val += 3
            val += letters[opp]

        elif me == "X":  # lose, get loser of opp, score it
            val += letters.get(lose[opp])

        elif me == "Z":  # win, get winner of opp, score it
            val += 6
            val += letters.get(win[opp])

    return val


if __name__ == '__main__':
    print(one())
    print(two())
