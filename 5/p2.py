input = open("example.txt", "r").readlines()

rules = []
updates = []
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
        updates.append(line)

mid_sum = 0
for pages in updates:
    correct = True
    # Keep increasing until the answer doesn't change...
    # (couldn't figure out how to get a while loop to work)
    for _ in range(10):
        for rule in rules:
            if rule[0] in pages and rule[1] in pages:
                x = pages.index(rule[0])
                y = pages.index(rule[1])
                if x > y:
                    pages.insert(max(y - 1, 0), pages.pop(x))
                    correct = False

    if not correct:
        mid_num = pages[(len(pages) - 1) // 2]
        mid_sum += mid_num

print(mid_sum)
