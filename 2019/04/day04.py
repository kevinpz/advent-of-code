from itertools import groupby


def check_valid(nb, size_limit):
    list_nb = list(str(nb))
    if sorted(list_nb) != list_nb:
        return False

    for _, count in groupby(list_nb):
        size = len(list(count))
        if size_limit == 0 and size > 1:
            return True
        elif size == size_limit:
            return True

    return False


def get_solution(filename):
    with open(filename) as file:
        start, end = [int(nb) for nb in file.readline().split("-")]
        res_p1 = 0
        res_p2 = 0
        for nb in range(start, end + 1):
            if check_valid(nb, 0):
                res_p1 += 1
            if check_valid(nb, 2):
                res_p2 += 1
    return res_p1, res_p2


if __name__ == "__main__":
    check_valid(12345, 0)
    sol_p1, sol_p2 = get_solution("day04_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")
