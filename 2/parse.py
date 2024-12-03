def parse_input() -> list[list[int]]:
    input = open("input.txt", "r").readlines()

    inputlines = [i.split() for i in input]
    input = []
    for line in inputlines:
        input.append([int(i) for i in line])

    return input
