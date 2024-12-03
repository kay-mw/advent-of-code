import re

input = open("input.txt", "r").readlines()

valid = []
enabled = True
for line in input:
    matches = re.split(r"(do\(\)|don't\(\))", line)
    for match in matches:
        if match == "don't()":
            enabled = False
            print(match, "\n", enabled)
        elif match == "do()":
            enabled = True
            print(match, "\n", enabled)
        else:
            if enabled:
                valid.append(match)
                print(match, "\n", enabled)

muls = []
for string in valid:
    matches = re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)", string)
    for match in matches:
        brackets = match.split("(")[1]
        nums = brackets.split(",")
        nums[1] = nums[1].replace(")", "")
        nums = [int(x) for x in nums]
        muls.append(nums[0] * nums[1])

print(sum(muls))
