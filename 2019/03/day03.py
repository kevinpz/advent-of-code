def get_points(wire):
    # x, y, step
    pos = [0, 0]
    step = 1

    # Great idea to optimize code from Ali Spittel
    # https://github.com/aspittel/advent-of-code/blob/master/2019/dec-03/script.py#L4
    dir_def = {"R": [0, 1], "L": [0, -1], "U": [1, 1], "D": [1, -1]}

    points = {}
    for move in wire.split(","):
        direction, dist = move[0], int(move[1:])
        idx, add = dir_def[direction]
        for _ in range(dist):
            pos[idx] += add
            points[tuple(pos)] = step
            step += 1

    return points


def get_solution(filename):
    with open(filename) as file:
        points1 = get_points(file.readline())
        points2 = get_points(file.readline())

        res = [[abs(p[0]) + abs(p[1]), points1[p] + points2[p]] for p in points1 if p in points2]

        res_p1 = min(res, key=lambda p: p[0])[0]
        res_p2 = min(res, key=lambda p: p[1])[1]

    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("day03_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")
