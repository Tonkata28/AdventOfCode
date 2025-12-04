with open("input.txt") as f:
    id_ranges = f.readline().strip().split(',')

invalid_ids_sum = 0

for id_range in id_ranges:
    parsed_range = [int(el) for el in id_range.split('-')]
    for curr_id in range(parsed_range[0], parsed_range[1] + 1):
        curr_id_as_str = str(curr_id)
        mid_index = len(curr_id_as_str) // 2 - 1
        repeated_sequence = ''

        for index, el in enumerate(curr_id_as_str):
            repeated_sequence += el
            if index == mid_index + 1:
                break

            if not curr_id_as_str.replace(repeated_sequence, ''):
                invalid_ids_sum += curr_id
                break


print(f"Result (part 2): {invalid_ids_sum}")

# with open("input.txt") as f:
#     id_ranges = f.readline().strip().split(',')
#
# invalid_ids_sum = 0
#
# for id_range in id_ranges:
#     parsed_range = [int(el) for el in id_range.split('-')]
#     for curr_id in range(parsed_range[0], parsed_range[1] + 1):
#         curr_id_as_str = str(curr_id)
#         mid_index = len(curr_id_as_str) // 2 - 1
#         if curr_id_as_str[0:mid_index + 1] == curr_id_as_str[mid_index + 1:]:
#             invalid_ids_sum += curr_id
#
# print(f"Result (part 1): {invalid_ids_sum}")
