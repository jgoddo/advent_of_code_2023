import aoc_helpers
import collections
import functools

YEAR = 2023
DAY = 4
SKIP_1 = False

TEST_CASES_1 = [
    (
        """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""",
        13,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 30)]


def parse_line(line):
    winning_numbers, user_numbers = line.split(' | ')
    _, winning_numbers = winning_numbers.split(': ')
    winning_numbers = winning_numbers.split()
    user_numbers = user_numbers.split()
    return winning_numbers, user_numbers


def part_1(part_input):
    lines = part_input.strip().split('\n')
    solution = 0
    for winning_numbers, user_numbers in map(parse_line, lines):
        winning_numbers = set(winning_numbers)
        user_numbers = set(user_numbers)
        matches = user_numbers.intersection(winning_numbers)
        if len(matches) > 0:
            solution += 2 ** (len(matches) - 1)
    return solution


def part_2(part_input):
    lines = part_input.strip().split('\n')
    cards = list(range(len(lines)))
    card_dict = {idx: 1 for idx in range(len(cards))}
    for card_idx, (winning_numbers, user_numbers) in enumerate(map(parse_line, lines)):
        winning_numbers = set(winning_numbers)
        user_numbers = set(user_numbers)
        matches = user_numbers.intersection(winning_numbers)
        for idx in range(card_idx + 1, min(card_idx + len(matches) + 1, len(cards))):
            card_dict[idx] += card_dict[card_idx]

    return sum(card_dict.values())


# alternative recursive solution
# for some reason did a detour to this unneccessarily complex solution first...


@functools.lru_cache
def get_n_cards(idx):
    if len(card_dict[idx]) == 0:
        return 1
    else:
        return 1 + sum(get_n_cards(card) for card in card_dict[idx])


card_dict = {}


def part_2_recursive(part_input):
    global card_dict
    lines = part_input.strip().split('\n')
    cards = list(range(len(lines)))
    card_dict = {}
    for card_idx, (winning_numbers, user_numbers) in enumerate(map(parse_line, lines)):
        winning_numbers = set(winning_numbers)
        user_numbers = set(user_numbers)
        matches = user_numbers.intersection(winning_numbers)
        # which cards do i get from which card
        card_dict[card_idx] = list(range(card_idx + 1, min(card_idx + len(matches) + 1, len(cards))))

    return sum(get_n_cards(card) for card in range(len(cards)))


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
