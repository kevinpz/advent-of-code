def check_valid(nb, size_limit):
    nb_list = [int(n) for n in str(nb)]

    adjacent = False
    count = 1
    for idx in range(0, len(nb_list) - 1):
        nb, next_nb = nb_list[idx], nb_list[idx + 1]
        if nb > next_nb:
            return False

        if nb == next_nb:
            if size_limit == 0:
                adjacent = True
            count += 1
        else:
            if count == size_limit:
                adjacent = True
            count = 1

    if count == size_limit:
        adjacent = True

    return adjacent


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
    sol_p1, sol_p2 = get_solution("day04_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")
