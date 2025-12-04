with open("input.txt") as f:
    banks = f.readlines()
BANK_NUMBERS = 12
total_power = 0

for bank in banks:
    bank = list(int(el) for el in bank.strip())
    biggest_number = ''
    biggest_value_index = -1

    for pos_num_to_take in range(1, BANK_NUMBERS + 1):
        biggest_value = 0
        left_spots = BANK_NUMBERS - pos_num_to_take
        if len(biggest_number) == BANK_NUMBERS:
            break
        for index_y, y in enumerate(bank[biggest_value_index + 1: -left_spots if left_spots >= 1 else None], biggest_value_index + 1):
            if biggest_value == 9: # test message
                break

            if y > biggest_value:
                biggest_value = y
                biggest_value_index = index_y

        biggest_number += str(biggest_value)

    total_power += int(biggest_number)

print(f"Result 2: {total_power}")

# with open("input.txt") as f:
#     banks = f.readlines()
# total_power = 0
#
# for bank in banks:
#     bank = list(int(el) for el in bank.strip())
#     first_biggest = max(bank[:-1:])
#     second_biggest = max(bank[bank.index(first_biggest) + 1:])
#     total_power += int(f"{first_biggest}{second_biggest}")
#
# print(f"Result 1: {total_power}")