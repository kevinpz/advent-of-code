def find_simple_fuel(mass):
    return mass // 3 - 2


def find_complex_fuel(mass):
    current_fuel = 0
    while mass > 0:
        mass = find_simple_fuel(mass)
        if mass > 0:
            current_fuel += mass
    current_fuel -= mass
    return current_fuel


def get_solution(filename):
    simple_fuel = 0
    complex_fuel = 0
    with open(filename) as file:
        for line in file:
            mass = int(line)
            # part 1
            simple_fuel += find_simple_fuel(mass)
            # part 2
            complex_fuel += find_complex_fuel(mass)
    return simple_fuel, complex_fuel


if __name__ == "__main__":
    nr_sum, r_sum = get_solution("input.txt")
    print(f"Part 1: {nr_sum}")
    print(f"Part 2: {r_sum}")