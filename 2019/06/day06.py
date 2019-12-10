def get_all_orbits(orbit_map):
    next_orbit = [["COM", 0]]
    orbit_size = 0
    while next_orbit:
        current_orbit, current_size = next_orbit.pop()
        if current_orbit in orbit_map:
            in_orbit = orbit_map[current_orbit]
            next_orbit += [[o, current_size + 1] for o in in_orbit]

        orbit_size += current_size

    return orbit_size


def get_solution(filename):
    with open(filename) as file:
        orbit_map = {}
        for line in file:
            src, dest = line.rstrip().split(")")
            if src not in orbit_map:
                orbit_map[src] = []
            orbit_map[src].append(dest)

        # part 1
        res_p1 = get_all_orbits(orbit_map)

        # part 2
        res_p2 = 0

    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("day06_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")