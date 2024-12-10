import random

input = open("input.txt", "r").readlines()

parsed = []
for i in range(len(input)):
    parse = input[i].replace("\n", "")
    parse = parse.split(":")
    parse[1] = parse[1].split(" ")
    parse[1] = parse[1][1:]
    parse[0] = int(parse[0])
    parse[1] = [int(x) for x in parse[1]]
    parsed.append(parse)


calibration = 0
for equation in parsed:
    target = equation[0]
    numbers = equation[1]

    n_operators = len(numbers) - 1
    n_combinations = 2

    diff = len(numbers) - 2
    for i in range(diff):
        n_combinations *= 2

    multiply = []
    while len(multiply) != n_combinations:
        base = []
        for i in range(n_operators):
            rand = random.randint(0, 1)
            base.append(False) if rand == 0 else base.append(True)

        if base not in multiply:
            multiply.append(base)

    results = []
    for mul in multiply:
        result = numbers[0]
        for i in range(1, len(numbers)):
            if mul[max(i - 1, 0)] == True:
                result *= numbers[i]
            else:
                result += numbers[i]

            results.append(result)

    if target in results:
        answer = [x for x in results if x == target][0]
        calibration += answer

print(calibration)
