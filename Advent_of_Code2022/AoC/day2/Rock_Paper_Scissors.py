def part1():
    def calc_score(they: str, you: str) -> int:
        you = ord(you) - 23
        they = ord(they)

        def calc_win() -> int:
            if they == you:
                return 3
            elif you - 1 == they:
                return 6
            elif you == they - 2:
                return 6
            else:
                return 0

        def calc_shape() -> int:
            return you - 64

        return calc_shape() + calc_win()

    with open("input.txt", "rb") as f:
        score: int = 0
        for line in f:
            line = line.decode()
            score += calc_score(line[0], line[2])

        print(score)


def part2() -> None:
    def calc_score(they: str, needWin: str) -> int:
        they = ord(they)

        lose = "X"
        draw = "Y"
        win = "Z"

        def calc_shape() -> int:
            if needWin == draw:
                return they
            elif needWin == win:
                if they == ord("C"):
                    return ord("A")
                else:
                    return they + 1
            else:
                if they == ord("A"):
                    return ord("C")
                else:
                    return they - 1

        def calc_win() -> int:
            if needWin == lose:
                return 0
            elif needWin == draw:
                return 3
            else:
                return 6

        return calc_shape() - 64 + calc_win()

    with open("input.txt", "rb") as f:
        score: int = 0
        for line in f:
            line = line.decode()
            score += calc_score(line[0], line[2])

        print(score)


if __name__ == "__main__":
    part2()
