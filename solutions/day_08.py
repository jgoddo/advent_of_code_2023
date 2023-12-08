import aoc_helpers
import numpy as np

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
TEST_CASES_2 = [
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

    start_nodes = np.array([node_mapping[node] for node in adjacency_map if node.endswith('A')])
    end_nodes = np.array([node_mapping[node] for node in adjacency_map if node.endswith('Z')])

    nodes_lut_r = np.array([[node_mapping[k], node_mapping[v['R']]] for k, v in adjacency_map.items()])
    nodes_lut_l = np.array([[node_mapping[k], node_mapping[v['L']]] for k, v in adjacency_map.items()])

    instruction_idx = 0
    tmp = start_nodes == end_nodes
    while not all(n in end_nodes for n in start_nodes):
        print(instruction_idx)
        instruction = instructions[instruction_idx % len(instructions)]
        if instruction == 'R':
            start_nodes = nodes_lut_r[start_nodes]
        else:
            start_nodes = nodes_lut_r[start_nodes]

    return instruction_idx


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
