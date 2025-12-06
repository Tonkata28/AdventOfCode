from functools import reduce

total_result = 0

with open("input.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]

    operations_mapper = {
        "+": lambda nums: reduce(lambda x, y: x + y, nums),
        "*": lambda nums: reduce(lambda x, y: x * y, nums)
    }

    for symbol_index in range(len(lines[0])):
        numbers = [int(lines[num_index][symbol_index]) for num_index in range(len(lines) - 1)]
        total_result += operations_mapper[lines[-1][symbol_index]](numbers)

print(total_result)