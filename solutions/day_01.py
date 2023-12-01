import aoc_helpers

YEAR = 2023
DAY = 1

TEST_CASES_1 = [
    (
        """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""",
        142,
    )
]
TEST_CASES_2 = [
    (
        """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""",
        281,
    )
]


def part_1(part_input):
    total_sum = 0
    for line in part_input.split('\n')[:-1]:
        line = ''.join(filter(lambda x: x.isdigit(), line))
        total_sum += int(line[0] + line[-1])

    return total_sum


def part_2(part_input):
    word_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    total_sum = 0
    for line in part_input.split('\n')[:-1]:
        digits = [(idx, int(val)) for idx, val in enumerate(line) if val.isdigit()]
        words_found = sorted(
            ((idx, val) for val, idx in enumerate(line.find(d) for d in word_digits) if idx != -1), key=lambda x: x[0]
        )
        words_found_r = sorted(
            ((idx, val) for val, idx in enumerate(line.rfind(d) for d in word_digits) if idx != -1), key=lambda x: x[0]
        )

        first_pos, first_digit, last_pos, last_digit = len(line), 0, 0, 0
        if len(digits) > 0:
            first_pos, first_digit = digits[0]
            last_pos, last_digit = digits[-1]

        if len(words_found) > 0:
            first_digit = words_found[0][1] + 1 if words_found[0][0] < first_pos else first_digit

        if len(words_found_r) > 0:
            last_digit = words_found_r[-1][1] + 1 if words_found_r[-1][0] > last_pos else last_digit

        total_sum += int(f'{first_digit}{last_digit}')
    return total_sum


if __name__ == '__main__':
    puzzle_input = aoc_helpers.get_puzzle_input(year=YEAR, day=DAY, readlines=False)
    for test_case, solution in TEST_CASES_1:
        test_result = part_1(test_case)
        assert test_result == solution, f'{test_result} != {solution}'
    res_1 = part_1(puzzle_input)
    print('Solution for part 1 is: ', res_1)
    # aoc_helpers.post_answer(res_1, DAY, 1, year=YEAR)

    for test_case, solution in TEST_CASES_2:
        test_result = part_2(test_case)
        assert test_result == solution, f'{test_result} != {solution}'
    res_2 = part_2(puzzle_input)
    print('Solution for part 2 is: ', res_2)
    # aoc_helpers.post_answer(res_2, DAY, 2, year=YEAR)
