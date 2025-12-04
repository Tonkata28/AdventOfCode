content = []

with open('input.txt') as f:
    [content.append(l.strip()) for l in f.readlines()]


STARTING_VALUE = 50
MIN_VALUE = 0
MAX_VALUE = 99
current_dial = STARTING_VALUE
counter = 0

for line in content:
    direction = line[0]
    value = int(line[1:])
    overlaps = 0

    match direction:

        case "L":
            if current_dial - value < MIN_VALUE:
                if current_dial != MIN_VALUE:
                    overlaps += abs(current_dial - value) // 100 + 1
                else:
                    overlaps += abs(current_dial - value) // 100

            current_dial = (MAX_VALUE + 1 + (current_dial - value)) % (MAX_VALUE + 1)

        case "R":
            if current_dial + value > MAX_VALUE:
                overlaps += abs(current_dial + value) // 100

            current_dial = (MIN_VALUE - 1 + current_dial + value - MAX_VALUE) % (MAX_VALUE + 1)
        case _:
            break

    counter += overlaps

    if current_dial == 0 and not overlaps:
        counter += 1

print(counter)
