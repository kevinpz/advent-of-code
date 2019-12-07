def get_fuel(mass):
    return mass // 3 - 2


def get_solution(filename):
    sum_answer = 0
    with open(filename) as file:
        for line in file:
            sum_answer += get_fuel(int(line))

    return sum_answer


if __name__ == "__main__":
    answer = get_solution("input.txt")
    print(f"Solution is {answer}")
