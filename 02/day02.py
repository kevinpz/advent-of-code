def restore_program(noun, verb, values):
    values[1] = noun
    values[2] = verb
    idx = 0
    while values[idx] != 99:
        val1 = values[values[idx + 1]]
        val2 = values[values[idx + 2]]
        pos = values[idx + 3]
        if values[idx] == 1:
            values[pos] = val1 + val2
        elif values[idx] == 2:
            values[pos] = val1 * val2
        idx += 4
    return values[0]


def get_solution(filename):
    with open(filename) as file:
        line = file.readline()
        values = [int(nb) for nb in line.split(",")]

        # part 1
        res_p1 = restore_program(12, 2, values[:])

        # part 2
        desired_output = 19690720
        for n in range(100):
            for v in range(100):
                res = restore_program(n, v, values[:])
                if res == desired_output:
                    res_p2 = 100 * n + v
                    break
    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")