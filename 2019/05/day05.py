def get_values(values, mode, params):
    val = []
    for m, p in zip(mode, params):
        if m == 0:
            val.append(values[p])
        else:
            val.append(p)
    return val


def run_test(values, input_code):
    idx = 0
    last_output = None
    while values[idx] != 99:
        code = values[idx]
        op = code % 100
        mode = code // 100

        mode = [mode // d % 10 for d in [1, 10, 100]]

        if op == 1:
            p1, p2, d = values[idx + 1:idx + 4]
            p1, p2 = get_values(values, mode, [p1, p2])
            values[d] = p1 + p2
            idx += 4
        elif op == 2:
            p1, p2, d = values[idx + 1:idx + 4]
            p1, p2 = get_values(values, mode, [p1, p2])
            values[d] = p1 * p2
            idx += 4
        elif op == 3:
            d = values[idx + 1]
            values[d] = input_code
            idx += 2
        elif op == 4:
            s = values[idx + 1]
            last_output = values[s]
            idx += 2
        elif op == 5:
            p, d = values[idx + 1:idx + 3]
            p, d = get_values(values, mode, [p, d])
            if p != 0:
                idx = d
            else:
                idx += 3
        elif op == 6:
            p, d = values[idx + 1:idx + 3]
            p, d = get_values(values, mode, [p, d])
            if p == 0:
                idx = d
            else:
                idx += 3
        elif op == 7:
            p1, p2, d = values[idx + 1:idx + 4]
            p1, p2 = get_values(values, mode, [p1, p2])
            if p1 < p2:
                values[d] = 1
            else:
                values[d] = 0
            idx += 4
        elif op == 8:
            p1, p2, d = values[idx + 1:idx + 4]
            p1, p2 = get_values(values, mode, [p1, p2])
            if p1 == p2:
                values[d] = 1
            else:
                values[d] = 0
            idx += 4

    return last_output


def get_solution(filename):
    with open(filename) as file:
        line = file.readline()
        values = [int(nb) for nb in line.split(",")]

        # part 1
        res_p1 = run_test(values[:], 1)

        # part 2
        res_p2 = run_test(values[:], 5)

    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("day05_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")