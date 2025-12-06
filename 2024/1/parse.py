def parse_input() -> tuple[list[int], list[int]]:
    input = open("input.txt", "r").readlines()

    left = []
    right = []
    for line in input:
        line = line.split(" ")
        line = [i for i in line if i != ""]
        line[1] = line[1].replace("\n", "")
        left.append(int(line[0]))
        right.append(int(line[1]))

    assert len(left) == len(right)

    return left, right
