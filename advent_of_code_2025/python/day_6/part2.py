import time
from functools import reduce

def numbers(inp_lines: list):
    cur_num = ''
    cur_numbers = []
    for symbol_index in range(len(inp_lines[0]) - 1, -1, -1):
        for line in inp_lines[:-1]:
            cur_num += line[symbol_index]

        if not cur_num.strip():
            yield cur_numbers
            cur_numbers = []
        else:
            cur_numbers.append(int(cur_num))
        cur_num = ''

    yield cur_numbers


starting_time = time.perf_counter()
total_result = 0

with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


    operations_mapper = {
        "+": lambda nums: reduce(lambda x, y: x + y, nums),
        "*": lambda nums: reduce(lambda x, y: x * y, nums)
    }

    operators = lines[-1].split()

    for i, numbers_col in enumerate(numbers(lines), 1):
        total_result += operations_mapper[operators[-i]](numbers_col)


print(total_result)
print(f"Finished in: {(time.perf_counter() - starting_time)*1000:.2f}ms")