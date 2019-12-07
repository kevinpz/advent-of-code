import operator


def restore_program(noun, verb, values):
    values[1] = noun
    values[2] = verb

    op_dict = {
        1: operator.add,
        2: operator.mul
    }

    idx = 0
    while values[idx] != 99:
        op, p1, p2, d = values[idx:idx+4]
        op_func = op_dict[op]
        values[d] = op_func(values[p1], values[p2])
        idx += 4

    return values[0]


def get_solution(filename):
    with open(filename) as file:
        line = file.readline()
        values = [int(nb) for nb in line.split(",")]

        # part 1
        res_p1 = restore_program(12, 2, values[:])

        # part 2
        for n in range(100):
            for v in range(100):
                res = restore_program(n, v, values[:])
                if res == 19690720:
                    res_p2 = 100 * n + v
                    break
    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")