import aoc_helpers
import tqdm

YEAR = 2023
DAY = 14
SKIP_1 = True

TEST_CASES_1 = [
    (
        """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""",
        136,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 64)]


# O will roll
# # will stay in place
# . is empy space


def part_1(part_input):
    part_input = part_input.strip().split('\n')

    rollers = set()
    solids = set()

    height = len(part_input)
    width = len(part_input[0])

    for y_idx, line in enumerate(part_input):
        for x_idx, val in enumerate(line):
            if val == 'O':
                rollers.add((y_idx, x_idx))
            elif val == '#':
                solids.add((y_idx, x_idx))

    print_board(rollers, solids, height, width)

    print('-' * 64)

    anything_moved = True
    while anything_moved:
        new_rollers = set()
        anything_moved = False
        for y, x in sorted(rollers):
            ny, nx = y - 1, x
            if (ny, nx) in new_rollers or (ny, nx) in solids or ny < 0:  # stay
                new_rollers.add((y, x))
            else:  # move!
                anything_moved = True
                new_rollers.add((ny, nx))

        rollers = new_rollers

    solution = sum(height - y for y, _ in rollers)
    print(rollers, solids)
    print_board(rollers, solids, height, width)
    return solution


def print_board(rollers, solids, height, width):
    for y in range(height):
        for x in range(width):
            if (y, x) in rollers:
                print('O', end='')
            elif (y, x) in solids:
                print('#', end='')
            else:
                print('.', end='')

        print()


def part_2(part_input):
    part_input = part_input.strip().split('\n')

    rollers = set()
    solids = set()

    height = len(part_input)
    width = len(part_input[0])

    for y_idx, line in enumerate(part_input):
        for x_idx, val in enumerate(line):
            if val == 'O':
                rollers.add((y_idx, x_idx))
            elif val == '#':
                solids.add((y_idx, x_idx))

    print_board(rollers, solids, height, width)

    print('-' * 64)

    roller_states = []

    step = 0

    while True:
        rollers = move(rollers, solids, height, width)
        if rollers in roller_states:
            break

        roller_states.append(rollers)
        step += 1

    pattern_idx = roller_states.index(rollers)

    cycle_length = step - pattern_idx
    initial_steps = pattern_idx + 1
    step = (1_000_000_000 - initial_steps) % (cycle_length)
    for _ in range(step):
        rollers = move(rollers, solids, height, width)

    solution = sum(height - y for y, _ in rollers)
    return solution  # 88117 too low


def move(rollers, solids, height, width):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # north, then west, then south, then east
    for direction_idx in range(4):
        anything_moved = True
        while anything_moved:
            new_rollers = set()
            anything_moved = False

            if direction_idx == 0:
                it = sorted(rollers)
            elif direction_idx == 1:
                it = sorted(rollers, key=lambda x: x[1], reverse=False)
            elif direction_idx == 2:
                it = sorted(rollers, reverse=True)
            elif direction_idx == 3:
                it = sorted(rollers, key=lambda x: x[1], reverse=True)

            for y, x in it:
                dy, dx = directions[direction_idx]
                ny, nx = y + dy, x + dx
                if (
                    (ny, nx) in new_rollers or (ny, nx) in solids or (ny < 0) or ny >= height or (nx < 0) or nx >= width
                ):  # stay
                    new_rollers.add((y, x))
                else:  # move!
                    anything_moved = True
                    new_rollers.add((ny, nx))

            rollers = new_rollers
    return rollers


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
