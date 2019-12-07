def get_points(wire):
    pos_x = 0
    pos_y = 0
    step = 1

    dir_def = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    points = {}
    for move in wire.split(","):
        direction = move[0]
        dist = int(move[1:])
        x, y = dir_def[direction]
        for _ in range(dist):
            pos_x += x
            pos_y += y
            points[(pos_x, pos_y)] = step
            step += 1

    return points


def find_intersections(points1, points2):
    return set(points1.keys()).intersection(set(points2.keys()))


def get_distances(points):
    return [abs(x) + abs(y) for x, y in points]


def get_delay(points1, points2, intersections):
    return [points1[p] + points2[p] for p in intersections]


def get_solution(filename):
    with open(filename) as file:
        wire1 = file.readline()
        wire2 = file.readline()

        points1 = get_points(wire1)
        points2 = get_points(wire2)

        intersections = find_intersections(points1, points2)

        res_p1 = min(get_distances(intersections))
        res_p2 = min(get_delay(points1, points2, intersections))

    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")
