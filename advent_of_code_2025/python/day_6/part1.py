from math import prod

with open("test.txt") as f:
    lines = f.readlines()
    number_lines = ([int(i) for i in line.split()] for line in lines[:-1])

    operations_mapper = {
        "+": sum,
        "*": prod
    }

    operations = list(zip(*number_lines))
    operators = lines[-1].split()
    total_result = sum(operations_mapper[operator](numbers) for operator, numbers in zip(operators, operations))

print(total_result)