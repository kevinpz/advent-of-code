def get_result(layer_list):
    min_layer = min(layer_list, key=lambda x: x.count("0"))
    return min_layer.count("1") * min_layer.count("2")


def get_picture(layer_list, col_nb):
    picture = ""
    mapping = {"0": " ", "1": "#"}
    for pos in range(len(layer_list[0])):
        if pos % col_nb == 0:
            picture += "\n"
        for layer in layer_list:
            if layer[pos] != "2":
                picture += mapping[layer[pos]]
                break

    return picture


def get_solution(filename):
    with open(filename) as file:
        line = file.readline()
        line_nb, col_nb = 6, 25
        layer_size = line_nb * col_nb
        layer_list = [line[i:i + layer_size] for i in range(0, len(line), layer_size)]

        # part 1
        res_p1 = get_result(layer_list)

        # part 2
        res_p2 = get_picture(layer_list, col_nb)

    return res_p1, res_p2


if __name__ == "__main__":
    sol_p1, sol_p2 = get_solution("day08_input.txt")
    print(f"Part 1: {sol_p1}")
    print(f"Part 2: {sol_p2}")
