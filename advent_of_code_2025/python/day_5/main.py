# PART 2:
with open("input.txt") as f:
    valid_ranges = []

    while (line:=f.readline().strip()) != '':
        valid_ranges.append([int(n) for n in line.split('-')])

valid_ranges = sorted(valid_ranges, key=lambda x:(x[0], x[1]))

i = 0
while i < len(valid_ranges):
    id_range = valid_ranges[i]
    j = i + 1
    if j < len(valid_ranges) and valid_ranges[i][1] >= valid_ranges[j][0]:
        valid_ranges[i][1] = max(valid_ranges[i][1], valid_ranges[j][1])
        valid_ranges.pop(j)
        i -= 1

    i += 1

fresh_id_count = 0
for id_ranges in valid_ranges:
    fresh_id_count += id_ranges[1] - id_ranges[0] + 1

print(fresh_id_count)



#PART 1:
# with open("input.txt") as f:
#     valid_ranges = set()
#     valid_count = 0
#
#     while (line:=f.readline().strip()) != '':
#         range_start, range_end = line.split('-')
#         valid_ranges.add((int(range_start), int(range_end)))
#
#     for num in f.readlines():
#         num = int(num)
#         is_valid = next((r for r in valid_ranges if in_range_check(r[0], r[1], num)), False)
#
#         if is_valid:
#             valid_count+=1
#
# print(valid_count)

