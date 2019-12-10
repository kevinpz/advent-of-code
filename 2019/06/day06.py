def get_all_orbits(orbit_map):
    next_orbit = [["COM", []]]
    # create a dict where for each planet, we have the list of all the parents
    total_orbit = {}
    while next_orbit:
        current_orbit, current_parent = next_orbit.pop()
        if current_orbit in orbit_map:
            in_orbit = orbit_map[current_orbit]
            next_orbit += [[o, current_parent + [current_orbit]] for o in in_orbit]
        total_orbit[current_orbit] = current_parent

    return total_orbit


# we need to count the total number of parents for each planet for the part 1
def get_orbit_nb(total_orbit):
    return sum([len(total_orbit[orbit]) for orbit in total_orbit])


# for the part two we have to count the number of different planets between the src and dest
def get_orbit_jump(total_orbit, src, dest):
    src_path = total_orbit[src]
    dest_path = total_orbit[dest]

    return len([o for o in src_path + dest_path if (o in src_path) ^ (o in dest_path)])


def get_solution(filename):
    with open(filename) as file:
        orbit_map = {}
        for line in file:
            src, dest = line.rstrip().split(")")
            if src not in orbit_map:
                orbit_map[src] = []
            orbit_map[src].append(dest)

        total_orbit = get_all_orbits(orbit_map)
        # part 1
        res_p1 = get_orbit_nb(total_orbit)
        # part 2
        res_p2 = get_orbit_jump(total_orbit, "YOU", "SAN")

    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("day06_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")