input = open("input.txt", "r").read()

input = list(map(int, input.split()))

for _ in range(25):
    new_list = []
    for i, stone in enumerate(input):
        if stone == 0:
            new_list.append(1)
        elif len(str(stone)) % 2 == 0:
            first_half, second_half = (
                str(stone)[: len(str(stone)) // 2],
                str(stone)[len(str(stone)) // 2 :],
            )
            new_list.append(int(first_half))
            new_list.append(int(second_half))
        else:
            new_list.append(stone * 2024)

    input = new_list

print(len(input))
