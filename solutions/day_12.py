import aoc_helpers

YEAR = 2023
DAY = 12
SKIP_1 = False

TEST_CASES_1 = [
    (
        """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""",
        21,
    )
]
TEST_CASES_2 = [("""""", 'FAIL')]


# how many different arrangements of operational and broken springs fit the given criteria in each row.
# def is_valid(spring_groups,)

import itertools


def part_1(part_input):
    part_input = part_input.strip().split('\n')
    solution = 0
    for line in part_input:
        springs, counts = line.split()
        counts = list(map(int, counts.split(',')))
        spring_groups = list(filter(len, springs.split('.')))

        n_springs = sum(counts)  # broken springs
        n_broken = springs.count('#')
        n_options = springs.count('?')

        # naive solution will obviously not work but had to try :)
        broken_to_place = n_springs - n_broken
        operational_to_place = n_options - broken_to_place

        chars = '#' * broken_to_place + '.' * operational_to_place
        for combination in set(itertools.permutations(chars, r=len(chars))):
            test_val = springs
            for v in combination:
                test_val = test_val.replace('?', v, 1)

            spring_groups = list(map(lambda x: x.count('#'), filter(len, test_val.split('.'))))

            if len(spring_groups) == len(counts) and all(a == b for a, b in zip(spring_groups, counts)):
                solution += 1

        print(springs, spring_groups, counts, solution)
    return solution


def part_2(part_input):
    return 'not solved'


if __name__ == '__main__':
    puzzle_input = aoc_helpers.get_puzzle_input(year=YEAR, day=DAY, readlines=False)

    if not SKIP_1:
        for test_case, solution in TEST_CASES_1:
            test_result = part_1(test_case)
            assert test_result == solution, f'{test_result} != {solution}'
            print('test passed!')
        res_1 = part_1(puzzle_input)
        print('Solution for part 1 is: ', res_1)
        # aoc_helpers.post_answer(res_1, DAY, 1, year=YEAR)

    for test_case, solution in TEST_CASES_2:
        test_result = part_2(test_case)
        assert test_result == solution, f'{test_result} != {solution}'

    res_2 = part_2(puzzle_input)
    print('Solution for part 2 is: ', res_2)
    # aoc_helpers.post_answer(res_2, DAY, 2, year=YEAR)
