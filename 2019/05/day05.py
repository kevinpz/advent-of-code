import operator


def get_values(values, mode, params):
    return [values[p] if m == 0 else p for m, p in zip(mode, params)]


def math_operation(p1, p2, op_func):
    return int(op_func(p1, p2))


def jump_operation(p, d, op_func, idx):
    return d if op_func(p, 0) else idx + 3


def get_op_mode(code):
    return code % 100, [code // 100 // d % 10 for d in [1, 10, 100]]


def run_test(values, input_code):
    idx = 0
    last_output = None

    op_dict = {1: operator.add, 2: operator.mul, 7: operator.lt, 8: operator.eq}
    jump_dict = {5: operator.ne, 6: operator.eq}

    while values[idx] != 99:
        op, mode = get_op_mode(values[idx])

        if op in op_dict:
            op_func = op_dict[op]
            p1, p2 = get_values(values, mode, values[idx + 1:idx + 3])
            values[values[idx + 3]] = math_operation(p1, p2, op_func)
            idx += 4

        if op in jump_dict:
            jump_func = jump_dict[op]
            p, d = get_values(values, mode, values[idx + 1:idx + 3])
            idx = jump_operation(p, d, jump_func, idx)

        elif op == 3:
            d = values[idx + 1]
            values[d] = input_code
            idx += 2

        elif op == 4:
            s = values[idx + 1]
            last_output = values[s]
            idx += 2

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