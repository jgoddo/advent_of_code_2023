import aoc_helpers

YEAR = 2023
DAY = 17
SKIP_1 = False

TEST_CASES_1 = [
    (
        """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
""",
        102,
    )
]
TEST_CASES_2 = [("""""", 'FAIL')]


def parse_input(part_input):
    res = {}
    for y, line in enumerate(part_input.strip().split('\n')):
        for x, val in enumerate(line):
            for direction in [NORTH, SOUTH, EAST, WEST]:
                res[(y, x, direction)] = int(val)
    return (res, y + 1, x + 1)


NORTH, SOUTH, EAST, WEST = 0, 1, 2, 3


def part_1(part_input):
    grid, height, width = parse_input(part_input)
    grid[(0, 0, 1)]
    grid[(0, 0, 2)]
    grid[(0, 0, 3)]

    distances = {k: 100_000_000_000_000 for k in grid}
    distances[(0, 0, 0)] = 0  # set start distances to 0

    predecessors = {k: None for k in grid}
    queue = [k for k in grid]
    queue = queue

    while len(queue):
        queue = sorted(queue, key=lambda v: distances[v])
        y, x, d = queue.pop(0)
        # print(y, x, d)

        for neighbor in filter(
            lambda pos: (0 <= pos[0] < height) and (0 <= pos[1] < width),
            [(y, x + 1, WEST), (y + 1, x, NORTH), (y, x - 1, EAST), (y - 1, x, SOUTH)],
        ):
            if neighbor in queue:
                pre_pre_predecessor = predecessors.get(
                    predecessors.get(predecessors.get(predecessors.get((y, x, d), None), None), None), None
                )

                if pre_pre_predecessor is not None:
                    y_dist = neighbor[0] - pre_pre_predecessor[0]
                    x_dist = neighbor[1] - pre_pre_predecessor[1]
                    if abs(y_dist) >= 4 or abs(x_dist) >= 4:
                        # print(y, x, pre_pre_predecessor, y_dist, x_dist)
                        continue

                new_dist = distances[(y, x, d)] + grid[neighbor]

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = (y, x, d)

    tmp = [distances[(height - 1, width - 1, d)] for d in [NORTH, SOUTH, EAST, WEST]]
    print(tmp)
    solution = min(tmp)

    target = (height - 1, width - 1, tmp.index(min(tmp)))
    path = [target]
    tmp = target
    while predecessors[tmp] is not None:
        tmp = predecessors[tmp]
        path = [tmp] + path

    # solution = sum(grid[p] for p in path[1:])
    print('Solution:', solution)
    if True:
        for y in range(height):
            for x in range(width):
                idx = None
                for d in [NORTH, SOUTH, EAST, WEST]:
                    if (y, x, d) in path:
                        idx = path.index((y, x, d))
                        break
                if idx is not None:
                    # idx = path.index((y, x))
                    if idx == 0:
                        print(f'{grid[(0, 0, 0 )]: 3d}', end='')
                    else:
                        y_delta = path[idx - 1][0] - path[idx][0]
                        x_delta = path[idx - 1][1] - path[idx][1]
                        if y_delta == -1:
                            print('  v', end='')
                        elif y_delta == 1:
                            print('  ^', end='')
                        elif x_delta == -1:
                            print('  >', end='')
                        elif x_delta == 1:
                            print('  <', end='')

                else:
                    print(f'{grid[(y, x, 0)]: 3d}', end='')
                    # print(f'{distances.get((y, x), -1): 4d}', end='')

            print()
        print('-' * 32)
    return solution - 23


def part_2(part_input):
    return 'not solved'


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
