import aoc_helpers
import re

YEAR = 2023
DAY = 6
SKIP_1 = False

TEST_CASES_1 = [
    (
        """Time:      7  15   30
Distance:  9  40  200
""",
        288,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 71503)]


def part_1(part_input):
    times, distances = part_input.strip().split('\n')
    times = list(map(int, re.findall(r'\d+', times)))
    distances = list(map(int, re.findall(r'\d+', distances)))

    solution = 1
    for time, distance in zip(times, distances):
        wins = 0
        for hold_duration in range(time):
            run_duration = time - hold_duration
            run_dist = hold_duration * run_duration
            if run_dist > distance:
                wins += 1
        solution *= wins

    return solution


def part_2(part_input):
    time, distance = part_input.replace(' ', '').strip().split('\n')
    time = list(map(int, re.findall(r'\d+', time)))[0]
    distance = list(map(int, re.findall(r'\d+', distance)))[0]

    wins = 0

    # run_dist = hold_duration * time - hold_duration**2
    # find first and last number where run_dist > distance
    # everything outside is lost
    # everything inside is won

    for hold_duration in range(time):
        run_duration = time - hold_duration
        run_dist = hold_duration * run_duration

        if run_dist > distance:
            wins += 1
    return wins


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
