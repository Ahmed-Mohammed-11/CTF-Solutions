starting_place = 65
number_sequence = [16, 9, 3, 15, 3, 20, 6, 20, 8,
                   5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

# Solution
solution = ""
for number in number_sequence:
    solution += chr(number + starting_place - 1)

print(solution)
