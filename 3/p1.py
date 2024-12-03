import re

input = open("input.txt", "r").readlines()

muls = []
for string in input:
    matches = re.findall(r"mul\([\d]{1,3}\,[\d]{1,3}\)", string)
    for match in matches:
        brackets = match.split("(")[1]
        nums = brackets.split(",")
        nums[1] = nums[1].replace(")", "")
        nums = [int(x) for x in nums]
        muls.append(nums[0] * nums[1])

print(sum(muls))
