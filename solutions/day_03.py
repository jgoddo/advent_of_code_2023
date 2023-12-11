import aoc_helpers
import collections

YEAR = 2023
DAY = 3
SKIP_1 = False

TEST_CASES_1 = [
    (
        """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""",
        4361,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 467835)]


def part_1(part_input):
    part_input = part_input.strip().split('\n')
    height = len(part_input)
    width = len(part_input[0])

    numbers = set()
    for y in range(height):
        for x in range(width):
            if not part_input[y][x].isdigit() and part_input[y][x] != '.':
                # special character found
                for y_offset in range(-1, 2):
                    for x_offset in range(-1, 2):
                        if (
                            (-1 < y + y_offset < height)
                            and (-1 < x + x_offset < width)
                            and part_input[y + y_offset][x + x_offset].isdigit()
                        ):
                            numbers.add((y + y_offset, x + x_offset))

    neighbour_numbers = []
    for ny, nx in numbers:
        res = [(ny, nx)]
        offset = 1
        while -1 < nx + offset < width and part_input[ny][nx + offset].isdigit():
            res.append((ny, nx + offset))
            offset += 1
        offset = 1
        while -1 < nx - offset < width and part_input[ny][nx - offset].isdigit():
            res.append((ny, nx - offset))
            offset += 1

        res = sorted(set(res), key=lambda x: x[1])
        if res not in neighbour_numbers:
            neighbour_numbers.append(res)

    res = 0
    for number in neighbour_numbers:
        curr = int(''.join([part_input[y][x] for y, x in number]))
        res += curr

    return res


def part_2(part_input):
    part_input = part_input.strip().split('\n')
    height = len(part_input)
    width = len(part_input[0])

    solution = 0
    for y in range(height):
        for x in range(width):
            if not part_input[y][x].isdigit() and part_input[y][x] == '*':
                numbers = set()

                for y_offset in range(-1, 2):
                    for x_offset in range(-1, 2):
                        if (
                            (-1 < y + y_offset < height)
                            and (-1 < x + x_offset < width)
                            and part_input[y + y_offset][x + x_offset].isdigit()
                        ):
                            numbers.add((y + y_offset, x + x_offset))

                if len(numbers) >= 2:
                    neighbour_numbers = []
                    for ny, nx in numbers:
                        res = [(ny, nx)]
                        offset = 1
                        while -1 < nx + offset < width and part_input[ny][nx + offset].isdigit():
                            res.append((ny, nx + offset))
                            offset += 1
                        offset = 1
                        while -1 < nx - offset < width and part_input[ny][nx - offset].isdigit():
                            res.append((ny, nx - offset))
                            offset += 1

                        res = sorted(set(res), key=lambda x: x[1])
                        if res not in neighbour_numbers:
                            neighbour_numbers.append(res)

                    if len(neighbour_numbers) == 2:
                        # excatly 2 numbers
                        n1 = int(''.join([part_input[y][x] for y, x in neighbour_numbers[0]]))
                        n2 = int(''.join([part_input[y][x] for y, x in neighbour_numbers[1]]))

                        solution += n1 * n2

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
