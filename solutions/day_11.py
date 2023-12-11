import aoc_helpers
import itertools

YEAR = 2023
DAY = 11
SKIP_1 = False

TEST_CASES_1 = [
    (
        """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""",
        374,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 'FAIL')]


def solve(part_input, expansion_factor=2):
    part_input = part_input.strip().split('\n')
    height = len(part_input)
    width = len(part_input[0])

    universe = {}
    idx = 0
    for y, line in enumerate(part_input):
        for x, val in enumerate(line):
            if val == '#':
                universe[(y, x)] = idx
                idx += 1

    cols_to_expand = set(range(height)).difference(set(v[0] for v in universe))
    rows_to_expand = set(range(width)).difference(set(v[1] for v in universe))

    # changing order is irritating but was more convenient for part 2
    expanded_universe = {}
    for (y, x), idx in universe.items():
        ny = len(set(range(0, y)).intersection(cols_to_expand))
        nx = len(set(range(0, x)).intersection(rows_to_expand))
        expanded_universe[idx] = (y + ny * (expansion_factor - 1), x + nx * (expansion_factor - 1))

    solution = 0
    for a_idx, b_idx in itertools.combinations(expanded_universe, r=2):
        solution += abs(expanded_universe[a_idx][0] - expanded_universe[b_idx][0]) + abs(
            expanded_universe[a_idx][1] - expanded_universe[b_idx][1]
        )

    return solution


def part_1(part_input):
    return solve(part_input, 2)


def part_2(part_input):
    return solve(part_input, 1000000)


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
        print('test result is:', test_result)
    #    assert test_result == solution, f'{test_result} != {solution}'

    print('factor 10:', solve(TEST_CASES_1[0][0], 10))
    print('factor 100:', solve(TEST_CASES_1[0][0], 100))

    res_2 = part_2(puzzle_input)
    print('Solution for part 2 is: ', res_2)
    # aoc_helpers.post_answer(res_2, DAY, 2, year=YEAR)
