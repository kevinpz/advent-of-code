import operator


class IntcodeComputer:
    _op_dict = {1: operator.add, 2: operator.mul, 7: operator.lt, 8: operator.eq}
    _jump_dict = {5: operator.ne, 6: operator.eq}

    def __init__(self, values, input):
        self.idx = 0
        self.values = values[:] + [0] * 6000
        self.input_list = [input]
        self.last_output = None
        self.base = 0

    def _get_values(self, mode, nb):
        val = []
        for m, p in zip(mode, range(1, nb + 1)):
            if m == 0:
                val.append(self.values[self.idx + p])
            elif m == 1:
                val.append(self.idx + p)
            else:
                val.append(self.values[self.idx + p] + self.base)
        if nb == 1:
            return val[0]
        return val

    def _math_operation(self, p1, p2, op_func):
        return int(op_func(self.values[p1], self.values[p2]))

    def _jump_operation(self, p, d, op_func):
        return self.values[d] if op_func(self.values[p], 0) else self.idx + 3

    def _get_op_mode(self, code):
        return code % 100, [code // d % 10 for d in [100, 1000, 10000]]

    def run_test(self):
        while self.values[self.idx] != 99:
            op, mode = self._get_op_mode(self.values[self.idx])

            if op in self._op_dict:
                p1, p2, d = self._get_values(mode, 3)
                self.values[d] = self._math_operation(p1, p2, self._op_dict[op])
                self.idx += 4

            elif op in self._jump_dict:
                p, d = self._get_values(mode, 2)
                self.idx = self._jump_operation(p, d, self._jump_dict[op])

            elif op == 3:
                d = self._get_values(mode, 1)
                self.values[d] = self.input_list.pop(0)
                self.idx += 2

            elif op == 4:
                s = self._get_values(mode, 1)
                self.last_output = self.values[s]
                self.idx += 2

            elif op == 9:
                b = self._get_values(mode, 1)
                self.base += self.values[b]
                self.idx += 2

        return self.last_output


def get_solution(filename):
    with open(filename) as file:
        line = file.readline()
        values = [int(nb) for nb in line.split(",")]

        # part 1
        computer = IntcodeComputer(values, 1)
        res_p1 = computer.run_test()

        # part 2
        computer = IntcodeComputer(values, 2)
        res_p2 = computer.run_test()

    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("day09_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")