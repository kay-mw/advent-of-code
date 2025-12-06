from parse import parse_input


def identify_safe(
    inputlines: list[list[int]],
) -> tuple[list[list[int]], list[list[int]], int]:
    safe_li = []
    unsafe_li = []
    safe_count = 0
    for input in inputlines:
        safe = True
        increasing = True if sorted(input) == input else False
        decreasing = True if sorted(input, reverse=True) == input else False
        if len(set(input)) != len(input):
            increasing, decreasing = False, False

        if not increasing and not decreasing:
            safe = False
        else:
            for i in range(1, len(input)):
                diff = input[i] - input[i - 1]
                if abs(diff) > 3:
                    safe = False
                    break

        safe_li.append(input) if safe else unsafe_li.append(input)
        if safe:
            safe_count += 1

    return safe_li, unsafe_li, safe_count


inputlines = parse_input()

safe_li, unsafe_li, safe_count = identify_safe(inputlines)

print(f"SAFE: {safe_li}, UNSAFE: {unsafe_li}")

for unsafe in unsafe_li:
    for i in range(len(unsafe)):
        mutable_copy = unsafe.copy()
        mutable_copy.pop(i)
        _, _, safe = identify_safe([mutable_copy])
        if safe == 1:
            safe_count += 1
            break

print(safe_count)
