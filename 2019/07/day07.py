import operator
from itertools import permutations


class IntcodeComputer:
    _op_dict = {1: operator.add, 2: operator.mul, 7: operator.lt, 8: operator.eq}
    _jump_dict = {5: operator.ne, 6: operator.eq}

    def __init__(self, values, input):
        self.idx = 0
        self.values = values[:]
        self.input_list = [input]
        self.last_output = None
        self.exited = False

    def _get_values(self, mode, start, end):
        return [self.values[p] if m == 0 else p for m, p in zip(mode, self.values[start:end])]

    def _math_operation(self, p1, p2, op_func):
        return int(op_func(p1, p2))

    def _jump_operation(self, p, d, op_func):
        return d if op_func(p, 0) else self.idx + 3

    def _get_op_mode(self, code):
        return code % 100, [code // 100 // d % 10 for d in [1, 10, 100]]

    def run_test(self):
        while self.values[self.idx] != 99:
            op, mode = self._get_op_mode(self.values[self.idx])

            if op in self._op_dict:
                op_func = self._op_dict[op]
                p1, p2 = self._get_values(mode, self.idx + 1, self.idx + 3)
                d = self.values[self.idx + 3]
                self.values[d] = self._math_operation(p1, p2, op_func)
                self.idx += 4

            if op in self._jump_dict:
                jump_func = self._jump_dict[op]
                p, d = self._get_values(mode, self.idx + 1, self.idx + 3)
                self.idx = self._jump_operation(p, d, jump_func)

            elif op == 3:
                d = self.values[self.idx + 1]
                self.values[d] = self.input_list.pop(0)
                self.idx += 2

            elif op == 4:
                s = self.values[self.idx + 1]
                self.last_output = self.values[s]
                self.idx += 2
                return self.last_output

        self.exited = True


def find_permutation(values):
    perm_list = permutations([0, 1, 2, 3, 4])
    max_signal = 0
    for perm in perm_list:
        last_out = 0
        computer_list = []
        for input_data in perm:
            computer_list.append(IntcodeComputer(values, input_data))

        for computer in computer_list:
            computer.input_list.append(last_out)
            computer.run_test()
            last_out = computer.last_output

        max_signal = max(max_signal, last_out)

    return max_signal


def find_permutation_loop(values):
    perm_list = permutations([5, 6, 7, 8, 9])
    max_signal = 0
    for perm in perm_list:
        last_out = 0
        computer_list = []
        for input_data in perm:
            computer_list.append(IntcodeComputer(values, input_data))

        while not computer_list[-1].exited:
            for computer in computer_list:
                computer.input_list.append(last_out)
                computer.run_test()
                last_out = computer.last_output

        max_signal = max(max_signal, last_out)

    return max_signal


def get_solution(filename):
    with open(filename) as file:
        line = file.readline()
        values = [int(nb) for nb in line.split(",")]

        # part 1
        res_p1 = find_permutation(values)

        # part 2
        res_p2 = find_permutation_loop(values)

    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("day07_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")