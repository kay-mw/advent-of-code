input = open("input.txt", "r").readlines()

rules = []
update = []
for line in input:
    if "|" in line:
        line = line.split("|")
        line[1] = line[1].replace("\n", "")
        line = [int(x) for x in line]
        rules.append(line)
    elif "," in line:
        line = line.split(",")
        line[-1] = line[-1].replace("\n", "")
        line = [int(x) for x in line]
        update.append(line)

ordered_pages = []
mid_sum = 0
for pages in update:
    correct = True
    for rule in rules:
        if rule[0] in pages and rule[1] in pages:
            x = pages.index(rule[0])
            y = pages.index(rule[1])
            if x > y:
                correct = False
                break

    if correct:
        mid_num = pages[(len(pages) - 1) // 2]
        mid_sum += mid_num

print(mid_sum)
