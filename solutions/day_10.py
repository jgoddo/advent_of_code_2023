import aoc_helpers
import re

YEAR = 2023
DAY = 10
SKIP_1 = True

TEST_CASES_1 = [
    (
        """.....
.S-7.
.|.|.
.L-J.
.....
""",
        4,
    ),
    (
        """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""",
        8,
    ),
]
TEST_CASES_2 = [
    (
        """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
""",
        4,
    ),
    (
        """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""",
        8,
    ),
    (
        """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""",
        10,
    ),
]


def get_neighbours(y_idx, x_idx, val):
    if val == '|':
        neighbours = [(y_idx - 1, x_idx), (y_idx + 1, x_idx)]
    elif val == '-':
        neighbours = [(y_idx, x_idx - 1), (y_idx, x_idx + 1)]
    elif val == 'L':
        neighbours = [(y_idx - 1, x_idx), (y_idx, x_idx + 1)]
    elif val == 'J':  # nw
        neighbours = [(y_idx - 1, x_idx), (y_idx, x_idx - 1)]
    elif val == '7':
        neighbours = [(y_idx + 1, x_idx), (y_idx, x_idx - 1)]
    elif val == 'F':
        neighbours = [(y_idx + 1, x_idx), (y_idx, x_idx + 1)]
    return neighbours


def build_network(part_input):
    start = None
    pipe_network = {}
    for y_idx, line in enumerate(part_input):
        for x_idx, val in enumerate(line):
            if val != '.':
                if val == 'S':
                    start = (y_idx, x_idx)
                    neighbours = []
                    for y, x in [(y_idx - 1, x_idx), (y_idx + 1, x_idx), (y_idx, x_idx + 1), (y_idx, x_idx - 1)]:
                        if part_input[y][x] != '.':
                            n = get_neighbours(y, x, part_input[y][x])
                            if start in n:
                                neighbours.append((y, x))

                else:
                    neighbours = get_neighbours(y_idx, x_idx, val)

                pipe_network[(y_idx, x_idx)] = neighbours
    return pipe_network, start


def get_path(pipe_network, start):
    prev = start
    curr = pipe_network[start][0]

    path = [start]
    while curr != start:
        path.append(curr)
        _curr = curr
        curr = [e for e in pipe_network[curr] if e != prev][0]
        prev = _curr
    return path


def part_1(part_input):
    part_input = part_input.strip().split('\n')

    pipe_network, start = build_network(part_input)

    path = get_path(pipe_network, start)

    return len(path) // 2


def part_2(part_input):
    part_input = part_input.strip().split('\n')
    pipe_network, start = build_network(part_input)

    start_neighbours = pipe_network[start]

    if start_neighbours == [(start[0] - 1, start[1]), (start[0] + 1, start[1])]:
        start_type = '|'
    if start_neighbours == [(start[0], start[1] - 1), (start[0], start[1] + 1)]:
        start_type = '-'
    if start_neighbours == [(start[0] - 1, start[1]), (start[0], start[1] + 1)]:
        start_type = 'L'
    if start_neighbours == [(start[0] - 1, start[1]), (start[0], start[1] - 1)]:
        start_type = 'J'
    if start_neighbours == [(start[0] + 1, start[1]), (start[0], start[1] - 1)]:
        start_type = '7'
    if start_neighbours == [(start[0] + 1, start[1]), (start[0], start[1] + 1)]:
        start_type = 'F'

    path = get_path(pipe_network, start)

    height = len(part_input)
    width = len(part_input[0])

    for y in range(height):
        tmp = ''.join(val if (y, x) in path else '.' for (x, val) in enumerate(part_input[y]))
        if 'S' in tmp:
            tmp = tmp.replace('S', start_type)
        part_input[y] = tmp

    solution = 0
    solution_vals = []
    for y, line in enumerate(part_input):
        is_inside = False
        opening_bracket = None
        for x, val in enumerate(line):
            if is_inside and val == '.':
                solution += 1
                solution_vals.append((y, x))

            elif val == '|':
                is_inside = not is_inside
            elif opening_bracket == 'L' and val in '7':
                is_inside = not is_inside
            elif opening_bracket == 'F' and val in 'J':
                is_inside = not is_inside

            if val in 'FL':
                opening_bracket = val
    if False:
        for y, line in enumerate(part_input):
            for x, val in enumerate(line):
                print('I' if (y, x) in solution_vals else val, end='')
            print()
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
