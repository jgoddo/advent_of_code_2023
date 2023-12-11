import aoc_helpers
from collections import Counter
from functools import cmp_to_key
import itertools

YEAR = 2023
DAY = 7
SKIP_1 = True

TEST_CASES_1 = [
    (
        """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""",
        6440,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 5905)]


def get_card_type(val):
    if len(val) == 1:
        # 5 of a kind
        return 7
    if max(val.values()) == 4:
        return 6
    if len(val.values()) == 2:
        return 5
    if max(val.values()) == 3:
        return 4
    if len(val.values()) == 3:
        return 3
    if len(val.values()) == 4:
        return 2
    return 1


CARD_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def cmp(a, b):
    a_score = get_card_type(Counter(a))
    b_score = get_card_type(Counter(b))
    if a_score < b_score:
        return -1
    elif a_score > b_score:
        return 1

    # same score
    for a_char, b_char in zip(a, b):
        if a_char == b_char:
            continue
        if CARD_ORDER.index(a_char) > CARD_ORDER.index(b_char):
            return -1
        else:
            return 1
    return 0


def part_1(part_input):
    part_input = part_input.strip().split('\n')
    cards, bids, rank = [], {}, []
    for line in part_input:
        line = line.split()
        cards.append(line[0])
        bids[line[0]] = int(line[1])

    cards = sorted(cards, key=cmp_to_key(cmp))
    score = sum((idx + 1) * bids[c] for idx, c in enumerate(cards))

    print(cards, score)

    return score


CARD_ORDER_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def cmp_2(a, b):
    a_cnt = Counter(a)
    b_cnt = Counter(b)
    a_opts, b_opts = [a], [b]

    for option in itertools.combinations_with_replacement(CARD_ORDER_2[:-1], r=a_cnt['J']):
        tmp = a
        for idx in range(a_cnt['J']):
            tmp = tmp.replace('J', option[idx], 1)
        a_opts.append(tmp)

    for option in itertools.combinations_with_replacement(CARD_ORDER_2[:-1], r=b_cnt['J']):
        tmp = b
        for idx in range(b_cnt['J']):
            tmp = tmp.replace('J', option[idx], 1)
        b_opts.append(tmp)

    a_score = max(get_card_type(Counter(val)) for val in a_opts)
    b_score = max(get_card_type(Counter(val)) for val in b_opts)

    if a_score < b_score:
        return -1
    elif a_score > b_score:
        return 1

    # same score
    for a_char, b_char in zip(a, b):
        if a_char == b_char:
            continue
        if CARD_ORDER_2.index(a_char) > CARD_ORDER_2.index(b_char):
            return -1
        else:
            return 1
    return 0


def part_2(part_input):
    part_input = part_input.strip().split('\n')
    cards, bids, rank = [], {}, []
    for line in part_input:
        line = line.split()
        cards.append(line[0])
        bids[line[0]] = int(line[1])

    cards = sorted(cards, key=cmp_to_key(cmp_2))
    score = sum((idx + 1) * bids[c] for idx, c in enumerate(cards))

    print(cards, score)

    return score


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
