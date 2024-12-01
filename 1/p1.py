from parse import parse_input

left, right = parse_input()

left = sorted(left)
right = sorted(right)

distances = []
for i in range(len(left)):
    distances.append(abs(left[i] - right[i]))

print(sum(distances))
