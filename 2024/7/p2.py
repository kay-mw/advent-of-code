import itertools

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

    # lol this is so much better than what I did in P1... :)
    # thank you to whoever implemented this into python
    operators = ["ADD", "MULTIPLY", "CONCAT"]
    combos = itertools.product(operators, repeat=len(numbers) - 1)

    results = []
    for mul in combos:
        result = numbers[0]
        for i in range(1, len(numbers)):
            if mul[max(i - 1, 0)] == "MULTIPLY":
                result *= numbers[i]
            elif mul[max(i - 1, 0)] == "ADD":
                result += numbers[i]
            else:
                result = int(str(result) + str(numbers[i]))

            results.append(result)

    if target in results:
        answer = [x for x in results if x == target][0]
        calibration += answer

print(calibration)
