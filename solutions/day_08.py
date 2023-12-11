import aoc_helpers
import collections
import math

YEAR = 2023
DAY = 8
SKIP_1 = True

TEST_CASES_1 = [
    (
        """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""",
        2,
    ),
    (
        """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""",
        6,
    ),
]
TEST_CASES_2 = []
[
    (
        """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""",
        6,
    )
]


def get_adjacency_map(nodes):
    adjacency_map = {}
    for line in nodes:
        node, neighbours = line.split(' = ')
        l, r = neighbours.split(', ')
        adjacency_map[node] = {'L': l[1:], 'R': r[:-1]}
    return adjacency_map


def part_1(part_input):
    part_input = part_input.strip().split('\n')
    instructions = part_input[0]
    nodes = part_input[2:]
    adjacency_map = get_adjacency_map(nodes)

    instruction_idx = 0
    curr_node = 'AAA'
    while curr_node != 'ZZZ':
        instruction = instructions[instruction_idx % len(instructions)]
        curr_node = adjacency_map[curr_node][instruction]
        instruction_idx += 1
    return instruction_idx


def part_2(part_input):
    part_input = part_input.strip().split('\n')
    instructions = part_input[0]
    nodes = part_input[2:]
    adjacency_map = get_adjacency_map(nodes)
    node_mapping = {key: idx for idx, key in enumerate(adjacency_map)}

    start_nodes = [node for node in adjacency_map if node.endswith('A')]
    end_nodes = [node for node in adjacency_map if node.endswith('Z')]
    reach_step = {n: [] for n in end_nodes}
    instruction_idx = 0

    while any(len(v) < 2 for v in reach_step.values()):
        for idx, val in enumerate(start_nodes):
            if val in end_nodes:
                if len(reach_step[val]) < 2:
                    reach_step[val].append(instruction_idx)

        instruction = instructions[instruction_idx % len(instructions)]
        start_nodes = [adjacency_map[n][instruction] for n in start_nodes]
        instruction_idx += 1

    # this only works because of the properties of the graph (which should be checked and not be guessed)
    intervals = [reach_step[key][1] - reach_step[key][0] for key in reach_step]
    return math.lcm(*intervals)


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
        # assert test_result == solution, f'{test_result} != {solution}'
        print(f'Finished test2 {test_result}')

    res_2 = part_2(puzzle_input)
    print('Solution for part 2 is: ', res_2)
    # aoc_helpers.post_answer(res_2, DAY, 2, year=YEAR)
