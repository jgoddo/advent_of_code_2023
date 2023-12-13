import aoc_helpers
import math

YEAR = 2023
DAY = 13
SKIP_1 = True
TEST_CASES_1 = [
    (
        """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""",
        405,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 400)]


def part_1(part_input):
    part_input = part_input.strip().split('\n\n')
    solution = 0
    for group in part_input:
        group = group.split('\n')
        center_found = False
        height = len(group)
        for idx in range(1, height):
            if all(a == b for a, b in zip(reversed(group[:idx]), group[idx:])):
                center_found = True
                solution += 100 * idx
                break

        if not center_found:
            width = len(group[0])
            cols = [''.join(row[idx] for row in group) for idx in range(width)]
            for idx in range(1, width):
                if all(a == b for a, b in zip(reversed(cols[:idx]), cols[idx:])):
                    print(group, idx)
                    center_found = True
                    solution += idx
                    break

    print(solution)
    return solution


def part_2(part_input):
    part_input = part_input.strip().split('\n\n')
    solution = 0
    for group in part_input:
        group = group.split('\n')
        center_found = False
        height = len(group)
        for idx in range(1, height):
            # iterate over rows
            diffs = [sum(a1 != b1 for a1, b1 in zip(a, b)) for a, b in zip(reversed(group[:idx]), group[idx:])]
            if max(diffs) == 1:  #  all(a == b for a, b in zip(reversed(group[:idx]), group[idx:])):
                center_found = True
                solution += 100 * idx
                break

        if not center_found:
            # iterate over columns

            width = len(group[0])
            cols = [''.join(row[idx] for row in group) for idx in range(width)]
            for idx in range(1, width):
                diffs = [sum(a1 != b1 for a1, b1 in zip(a, b)) for a, b in zip(reversed(cols[:idx]), cols[idx:])]
                if max(diffs) == 1:
                    # if all(a == b for a, b in zip(reversed(cols[:idx]), cols[idx:])):
                    center_found = True
                    solution += idx
                    break
            pass

    print(solution)
    return solution


if __name__ == '__main__':
    puzzle_input = aoc_helpers.get_puzzle_input(year=YEAR, day=DAY, readlines=False)
    if not SKIP_1:
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
