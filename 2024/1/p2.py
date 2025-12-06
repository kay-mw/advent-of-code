from parse import parse_input

left, right = parse_input()

matches = []
for i in range(len(left)):
    target = left[i]
    n_appear = len([num for num in right if num == target])
    score = target * n_appear
    matches.append(score)

print(sum(matches))
