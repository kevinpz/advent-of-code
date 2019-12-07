def get_fuel(mass):
    return mass // 3 - 2


def get_recursive_fuel(mass):
    current_fuel = 0
    while mass > 0:
        mass = get_fuel(mass)
        if mass > 0:
            current_fuel += mass
    current_fuel -= mass
    return current_fuel


def get_solution(filename):
    non_recursive_sum = 0
    recursive_sum = 0
    with open(filename) as file:
        for line in file:
            mass = int(line)
            non_recursive_sum += get_fuel(mass)
            recursive_sum += get_recursive_fuel(mass)
    return non_recursive_sum, recursive_sum


if __name__ == "__main__":
    nr_sum, r_sum = get_solution("input.txt")
    print(f"Part 1: {nr_sum}")
    print(f"Part 2: {r_sum}")