import aoc_helpers

YEAR = 2023
DAY = 16
SKIP_1 = True

TEST_CASES_1 = [
    (
        """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
""",
        46,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 51)]


def parse_grid(input):
    input = input.strip().split('\n')
    grid = {}
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            grid[(y, x)] = char
    return grid, len(input), len(input[0])


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # east west south north
EAST = 0
WEST = 1
SOUTH = 2
NORTH = 3


def part_1(part_input):
    grid, height, width = parse_grid(part_input)

    beam_positions = set()
    beam_ends = [((0, 0), 0)]

    for y in range(height):
        for x in range(width):
            print(grid[(y, x)], end='')
        print()
    cnt = 30
    beam_states = set()

    while len(beam_ends) > 0:
        new_ends = set()
        for pos, direction in beam_ends:
            beam_states.add((pos, direction))
            y, x = pos
            beam_positions.add(pos)
            value = grid[pos]
            # print(y, x, value)

            if value == '|':
                if direction == EAST:
                    new_ends.add(((y - 1, x), NORTH))
                    new_ends.add(((y + 1, x), SOUTH))
                if direction == WEST:
                    new_ends.add(((y + 1, x), SOUTH))
                    new_ends.add(((y - 1, x), NORTH))
                if direction == SOUTH:
                    new_ends.add(((y + 1, x), SOUTH))
                if direction == NORTH:
                    new_ends.add(((y - 1, x), NORTH))

            elif value == '\\':
                if direction == EAST:  # from east
                    new_ends.add(((y + 1, x), SOUTH))
                if direction == WEST:  # from west
                    new_ends.add(((y - 1, x), NORTH))
                if direction == SOUTH:  # from south
                    new_ends.add(((y, x + 1), EAST))
                if direction == NORTH:  # from north
                    new_ends.add(((y, x - 1), WEST))

            elif value == '/':
                if direction == EAST:  # from east
                    new_ends.add(((y - 1, x), NORTH))
                if direction == WEST:  # from west
                    new_ends.add(((y + 1, x), SOUTH))

                if direction == SOUTH:  # from south
                    new_ends.add(((y, x - 1), WEST))
                if direction == NORTH:  # from north
                    new_ends.add(((y, x + 1), EAST))
            elif value == '-':
                if direction == EAST:
                    new_ends.add(((y, x + 1), EAST))
                if direction == WEST:
                    new_ends.add(((y, x - 1), WEST))
                if direction == SOUTH:
                    new_ends.add(((y, x - 1), WEST))
                    new_ends.add(((y, x + 1), EAST))
                if direction == NORTH:
                    new_ends.add(((y, x - 1), WEST))
                    new_ends.add(((y, x + 1), EAST))

            else:
                ny, nx = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
                if 0 <= ny < height and 0 <= nx < width:  # else out of bounds
                    new_ends.add(((ny, nx), direction))

            beam_ends = set(
                filter(lambda x: x not in beam_states and 0 <= x[0][0] < height and 0 <= x[0][1] < width, new_ends)
            )

            if len(beam_positions) == 46:
                cnt -= 1
                if cnt <= 0:
                    break
        print(len(beam_positions))
        print(beam_ends)

    for y in range(height):
        for x in range(width):
            if (y, x) in beam_positions:
                print('#', end='')

            else:
                print('.', end='')

    return len(beam_positions)


def solve(grid, height, width, beam_ends):
    beam_positions = set()
    # for y in range(height):
    #    for x in range(width):
    #        print(grid[(y, x)], end='')
    #    print()
    cnt = 30
    beam_states = set()
    print(beam_ends)

    while len(beam_ends) > 0:
        new_ends = set()
        for pos, direction in beam_ends:
            beam_states.add((pos, direction))
            y, x = pos
            beam_positions.add(pos)
            value = grid[pos]
            # print(y, x, value)

            if value == '|':
                if direction == EAST:
                    new_ends.add(((y - 1, x), NORTH))
                    new_ends.add(((y + 1, x), SOUTH))
                if direction == WEST:
                    new_ends.add(((y + 1, x), SOUTH))
                    new_ends.add(((y - 1, x), NORTH))
                if direction == SOUTH:
                    new_ends.add(((y + 1, x), SOUTH))
                if direction == NORTH:
                    new_ends.add(((y - 1, x), NORTH))

            elif value == '\\':
                if direction == EAST:  # from east
                    new_ends.add(((y + 1, x), SOUTH))
                if direction == WEST:  # from west
                    new_ends.add(((y - 1, x), NORTH))
                if direction == SOUTH:  # from south
                    new_ends.add(((y, x + 1), EAST))
                if direction == NORTH:  # from north
                    new_ends.add(((y, x - 1), WEST))

            elif value == '/':
                if direction == EAST:  # from east
                    new_ends.add(((y - 1, x), NORTH))
                if direction == WEST:  # from west
                    new_ends.add(((y + 1, x), SOUTH))

                if direction == SOUTH:  # from south
                    new_ends.add(((y, x - 1), WEST))
                if direction == NORTH:  # from north
                    new_ends.add(((y, x + 1), EAST))
            elif value == '-':
                if direction == EAST:
                    new_ends.add(((y, x + 1), EAST))
                if direction == WEST:
                    new_ends.add(((y, x - 1), WEST))
                if direction == SOUTH:
                    new_ends.add(((y, x - 1), WEST))
                    new_ends.add(((y, x + 1), EAST))
                if direction == NORTH:
                    new_ends.add(((y, x - 1), WEST))
                    new_ends.add(((y, x + 1), EAST))

            else:
                ny, nx = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
                if 0 <= ny < height and 0 <= nx < width:  # else out of bounds
                    new_ends.add(((ny, nx), direction))

            beam_ends = set(
                filter(lambda x: x not in beam_states and 0 <= x[0][0] < height and 0 <= x[0][1] < width, new_ends)
            )

            if len(beam_positions) == 46:
                cnt -= 1
                if cnt <= 0:
                    break
        # print(len(beam_positions))
        # print(beam_ends)

    # for y in range(height):
    #    for x in range(width):
    #        if (y, x) in beam_positions:
    ##            print('#', end='')
    #
    #        else:
    #            print('.', end='')
    print(len(beam_positions))
    return len(beam_positions)


def part_2(part_input):
    grid, height, width = parse_grid(part_input)
    options = []

    for y in range(height):
        options.append(solve(grid, height, width, [((y, 0), EAST)]))
        options.append(solve(grid, height, width, [((y, width - 1), WEST)]))

    for x in range(width):
        options.append(solve(grid, height, width, [((0, x), SOUTH)]))
        options.append(solve(grid, height, width, [((height - 1, x), NORTH)]))

    return max(options)


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
        # test_result = part_2(test_case)
        pass
        # assert test_result == solution, f'{test_result} != {solution}'

    res_2 = part_2(puzzle_input)
    print('Solution for part 2 is: ', res_2)
    aoc_helpers.post_answer(res_2, DAY, 2, year=YEAR)
