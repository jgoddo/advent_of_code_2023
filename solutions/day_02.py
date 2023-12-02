import aoc_helpers
import collections

YEAR = 2023
DAY = 2
SKIP_1 = False

TEST_CASES_1 = [
    (
        """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""",
        8,
    )
]
TEST_CASES_2 = [
    (
        TEST_CASES_1[0][0],
        2286,
    )
]

cube_dict = collections.defaultdict(int)


def parse_line(line):
    _, line = line.split(': ')
    rounds = [
        collections.defaultdict(int, {v: int(k) for k, v in map(lambda x: x.split(' '), r.strip().split(', '))})
        for r in line.split(';')
    ]
    return rounds


def check_game(game, r_max=12, g_max=13, b_max=14):
    for entry in game:
        if (entry['red'] > r_max) or (entry['green'] > g_max) or (entry['blue'] > b_max):
            return False
    return True


# 12r 13g 14b
def part_1(part_input):
    solution = 0
    for game_id, game in enumerate(map(parse_line, part_input.strip().split('\n'))):
        if check_game(game):
            solution += game_id + 1
    return solution


def min_cubes(game):
    r_max, g_max, b_max = 0, 0, 0
    for entry in game:
        r_max = max(r_max, entry['red'])
        g_max = max(g_max, entry['green'])
        b_max = max(b_max, entry['blue'])
    return r_max * g_max * b_max


def part_2(part_input):
    solution = 0
    for game in map(parse_line, part_input.strip().split('\n')):
        solution += min_cubes(game)
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
