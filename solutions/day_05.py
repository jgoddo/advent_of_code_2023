import aoc_helpers

YEAR = 2023
DAY = 5
SKIP_1 = True

TEST_CASES_1 = [
    (
        """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""",
        35,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 46)]


def build_map(section):
    ret = {}
    for line in section:
        dst, src, rng = list(map(int, line.split()))
        ret[range(src, src + rng)] = dst - src
        # for offset in range(rng):
        #    ret[src + offset] = dst + offset

    return ret


def part_1(part_input):
    part_input = part_input.split('\n\n')
    seeds = list(map(int, part_input[0][7:].split()))
    maps = {}
    for map_category in part_input[1:]:
        map_category = map_category.strip().split('\n')
        map_title = map_category[0].split(' map:')[0]
        maps[map_title] = build_map(map_category[1:])

    # i could ignore the semantic meaning of the maps?
    min_loc = 10000000000000000000000000000000000000
    for seed in seeds:
        print(seed)
        loc = seed
        for key in [
            'seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ]:
            for in_range, offset in maps[key].items():
                if loc in in_range:
                    loc += offset
                    break
        min_loc = min(loc, min_loc)

    return min_loc


def part_2(part_input):
    part_input = part_input.split('\n\n')

    # well huge numbers in Input go brrrrrt!
    seeds_ranges = list(map(int, part_input[0][7:].split()))
    seeds = []
    for i in range(0, len(seeds_ranges), 2):
        seeds += list(range(seeds_ranges[i], seeds_ranges[i] + seeds_ranges[i + 1]))
    # seeds = sum(list(range(seeds_ranges[i], seeds_ranges[i + 1]) for i in range(0, len(seeds_ranges), 2)), [])
    print(seeds, len(seeds))
    maps = {}
    for map_category in part_input[1:]:
        map_category = map_category.strip().split('\n')
        map_title = map_category[0].split(' map:')[0]
        maps[map_title] = build_map(map_category[1:])

    # i could ignore the semantic meaning of the maps?
    min_loc = 10000000000000000000000000000000000000
    for seed in seeds:
        print(seed)
        loc = seed
        for key in [
            'seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ]:
            for in_range, offset in maps[key].items():
                if loc in in_range:
                    loc += offset
                    break
        min_loc = min(loc, min_loc)

    return min_loc


if __name__ == '__main__':
    puzzle_input = aoc_helpers.get_puzzle_input(year=YEAR, day=DAY, readlines=False)

    if not SKIP_1:
        for test_case, solution in TEST_CASES_1:
            test_result = part_1(test_case)
            assert test_result == solution, f'{test_result} != {solution}'
        print('part1')
        res_1 = part_1(puzzle_input)
        print('Solution for part 1 is: ', res_1)
        # aoc_helpers.post_answer(res_1, DAY, 1, year=YEAR)

    for test_case, solution in TEST_CASES_2:
        test_result = part_2(test_case)
        assert test_result == solution, f'{test_result} != {solution}'

    res_2 = part_2(puzzle_input)
    print('Solution for part 2 is: ', res_2)
    # aoc_helpers.post_answer(res_2, DAY, 2, year=YEAR)
