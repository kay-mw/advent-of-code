input = open("input.txt", "r").read()

input = input.replace("\n", "")
input = list(map(int, input))

disk_map = []
id = 0
for i, num in enumerate(input):
    if num > 0:
        if i % 2 == 0:
            for _ in range(num):
                disk_map.append({"id": id, "num": num})

            id += 1
        else:
            for _ in range(num):
                disk_map.append(".")

switches = len([j for j, x in enumerate(disk_map) if x == "."])
for i in range(switches):
    print(i)
    dot_pos = [j for j, x in enumerate(disk_map) if x == "."]
    file_pos = [j for j, x in enumerate(disk_map) if x != "."]

    dot_target = dot_pos[0]
    file_target = file_pos[-1]

    disk_map[dot_target], disk_map[file_target] = (
        disk_map[file_target],
        disk_map[dot_target],
    )

file_map = [x for x in disk_map if x != "."]

checksum = 0
pos = 0
for i, file in enumerate(file_map):
    checksum += file["id"] * pos
    pos += 1

print(checksum)
