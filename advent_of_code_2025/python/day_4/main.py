def is_valid_position(curr_row, curr_col, max_rows, max_cols):
    return 0 <= curr_row < max_rows and 0 <= curr_col < max_cols

TOILET_PAPER_SIGN = '@'

paper_positions = set()

directions_mapper = {
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 1),
    (1, 0),
}

with open("input.txt") as f:
    content = [list(l.strip()) for l in f.readlines()]

accessible_rolls = 0
rolls_to_remove = True
while rolls_to_remove:
    rolls_to_remove = False
    for row_index in range(len(content)):
        row = content[row_index]
        for col_index in range(len(row)):
            if content[row_index][col_index] == TOILET_PAPER_SIGN:
                nearby_rolls = 0

                for pos in directions_mapper:
                    dr, dc = pos
                    cur_row, cur_col = dr + row_index, dc + col_index

                    if is_valid_position(cur_row, cur_col, len(content), len(row)) and content[cur_row][cur_col] == TOILET_PAPER_SIGN:
                        nearby_rolls += 1

                        if nearby_rolls > 3:
                            break

                if nearby_rolls <= 3:
                    rolls_to_remove = True
                    accessible_rolls += 1
                    paper_positions.add((row_index, col_index))

    for pos in paper_positions:
        content[pos[0]][pos[1]] = '.'

print(accessible_rolls)
print(paper_positions)

# def is_valid_position(curr_row, curr_col, max_rows, max_cols):
#     return 0 <= curr_row < max_rows and 0 <= curr_col < max_cols
#
# TOILET_PAPER_SIGN = '@'
#
# directions_mapper = {
#     (-1, -1),
#     (-1, 0),
#     (-1, 1),
#     (0, -1),
#     (0, 1),
#     (1, -1),
#     (1, 1),
#     (1, 0),
# }
# accessible_rolls = 0
#
# with open("input.txt") as f:
#     content = [l.strip() for l in f.readlines()]
#
#
# for row_index in range(len(content)):
#     row = content[row_index]
#     for col_index in range(len(row)):
#         if content[row_index][col_index] == TOILET_PAPER_SIGN:
#             nearby_rolls = 0
#
#             for pos in directions_mapper:
#                 dr, dc = pos
#                 cur_row, cur_col = dr + row_index, dc + col_index
#
#                 if is_valid_position(cur_row, cur_col, len(content), len(row)) and content[cur_row][cur_col] == TOILET_PAPER_SIGN:
#                     nearby_rolls += 1
#
#                     if nearby_rolls > 3:
#                         break
#
#             if nearby_rolls <= 3:
#                 accessible_rolls += 1
#
# print(accessible_rolls)
