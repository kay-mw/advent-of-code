from parse import parse_input

inputlines = parse_input()

safe_count = 0
for input in inputlines:
    safe = True
    increasing = True if sorted(input) == input else False
    decreasing = True if sorted(input, reverse=True) == input else False
    if len(set(input)) != len(input):
        increasing, decreasing = False, False

    if not increasing and not decreasing:
        safe = False
        continue
    else:
        for i in range(1, len(input)):
            diff = input[i] - input[i - 1]
            if abs(diff) > 3:
                safe = False
                break

    if safe:
        safe_count += 1

print(safe_count)
