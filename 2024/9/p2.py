from itertools import groupby
from operator import itemgetter

input = open("input.txt", "r").read()

input = input.replace("\n", "")
input = list(map(int, input))

disk_map = []
id = 0
for i, num in enumerate(input):
    if num > 0:
        if i % 2 == 0:
            for _ in range(num):
                disk_map.append({"id": id, "file": num})

            id += 1
        else:
            for _ in range(num):
                disk_map.append(".")


files = [x for x in disk_map if "id" in x]
files_by_id = []
for k, v in groupby(files, key=lambda x: x["id"]):
    files_by_id.append(list(v))

files_by_id = sorted(files_by_id, key=lambda x: x[0]["id"], reverse=True)
for i in range(len(files_by_id)):
    current_file = files_by_id[i]

    dots_idx = [i for i, x in enumerate(disk_map) if x == "."]
    consecutive_dots_idx = []
    for k, g in groupby(enumerate(dots_idx), lambda ix: ix[0] - ix[1]):
        consecutive_dots_idx.append((list(map(itemgetter(1), g))))

    for j in range(len(consecutive_dots_idx)):
        current_dots = consecutive_dots_idx[j]

        if len(current_file) <= len(current_dots):
            current_file_positions = [
                k for k, x in enumerate(disk_map) if x == current_file[0]
            ]
            if min(current_file_positions) > max(current_dots):
                for k in range(len(current_file_positions)):
                    disk_map[current_dots[k]], disk_map[current_file_positions[k]] = (
                        disk_map[current_file_positions[k]],
                        disk_map[current_dots[k]],
                    )
                break
            else:
                continue


checksum = 0
pos = 0
for i, file in enumerate(disk_map):
    if file == ".":
        pos += 1
        continue
    else:
        checksum += file["id"] * pos
        pos += 1

print(checksum)
