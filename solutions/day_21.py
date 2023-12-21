import aoc_helpers

YEAR = 2023
DAY = 21
SKIP_1 = True

TEST_CASES_1 = [
    (
        """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
""",
        16,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 6536)]


def parse_grid(part_input):
    part_input = part_input.strip().split('\n')
    grid = set()
    start = None
    for y, line in enumerate(part_input):
        for x, val in enumerate(line):
            if val == '#':
                grid.add((y, x))
            elif val == 'S':
                start = y, x
    return grid, start, y + 1, x + 1


import collections


def part_1(part_input, step_range):
    grid, start, height, width = parse_grid(part_input)
    step_locs = collections.defaultdict(set)
    step_locs[-1].add(start)
    for step in range(step_range):
        print(step)
        for y, x in set(step_locs[step - 1]):
            for neighbor in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if neighbor not in grid:
                    step_locs[step].add(neighbor)
    print(step_locs[step_range - 1])
    return len(step_locs[step_range - 1])


def part_2(part_input, step_range):
    grid, start, height, width = parse_grid(part_input)
    step_locs = collections.defaultdict(set)
    step_locs[-1].add(start)
    for step in range(1000):
        if step % 100 == 0:
            print(step)
        for y, x in set(step_locs[step - 1]):
            for neighbor in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                ny, nx = neighbor[0] % height, neighbor[1] % width
                if (ny, nx) not in grid:
                    step_locs[step].add(neighbor)
    print(step_locs[step], len(step_locs[step]))
    return len(set(step_locs[step_range - 1]))


if __name__ == '__main__':
    puzzle_input = aoc_helpers.get_puzzle_input(year=YEAR, day=DAY, readlines=False)

    if not SKIP_1:
        for test_case, solution in TEST_CASES_1:
            test_result = part_1(test_case, 6)
            assert test_result == solution, f'{test_result} != {solution}'
        res_1 = part_1(puzzle_input, 64)
        print('Solution for part 1 is: ', res_1)
        # aoc_helpers.post_answer(res_1, DAY, 1, year=YEAR)

    for test_case, solution in TEST_CASES_2:
        test_result = part_2(test_case, 100)
        assert test_result == solution, f'{test_result} != {solution}'

    res_2 = part_2(puzzle_input, 26501365)
    print('Solution for part 2 is: ', res_2)
    # aoc_helpers.post_answer(res_2, DAY, 2, year=YEAR)
