import aoc_helpers

YEAR = 2023
DAY = 20
SKIP_1 = False

TEST_CASES_1 = [
    (
        """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""",
        32000000,
    ),
    (
        """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""",
        11687500,
    ),
]
TEST_CASES_2 = [("""""", 'FAIL')]


# % flip flop --> init off; high: _; low_ flip
# & conjunction:


class Module:
    def __init__(self, name: str, type: str):
        self.name = name
        self.pre = []
        self.children = []
        self.type = type
        self.state = False  # initially off


import collections

Module = collections.namedtuple('Module', ['module_type', 'name', 'children'])


def parse_modules(part_input):
    modules = {}
    for line in part_input:
        name, children = line.split(' -> ')

        if name.startswith('%'):
            module_type, module_name = name[:1], name[1:]
        elif name.startswith('&'):
            module_type, module_name = name[:1], name[1:]
        elif name == 'broadcaster':
            module_type, module_name = name, name
        else:
            module_type, module_name = 'sink', name

        children = [c.strip() for c in children.split(',')]
        # print(line)
        # print(module_type, module_name, children)
        # print('-' * 64)
        modules[module_name] = Module(module_type, module_name, children)
    return modules


def part_1(part_input):
    part_input = part_input.strip().split('\n')
    modules = parse_modules(part_input)
    process_buffer = []
    cnt = {True: 0, False: 0}

    module_states = {m: False for m in modules}
    module_predecessors = {m: {} for m in modules}

    for key, value in modules.items():
        for c in value.children:
            if c not in module_predecessors:
                module_predecessors[c] = {}
            module_predecessors[c][key] = False

    print(modules)
    print('-' * 32)
    print(module_predecessors)
    print('-' * 32)
    print(module_states)
    print('-' * 32)

    for idx in range(1000):
        # print(idx)
        # print(module_states)
        cnt[False] += 1
        process_buffer = [(modules['broadcaster'], False)]
        while len(process_buffer):
            curr_module, pulse = process_buffer.pop(0)
            cnt[pulse] += len(curr_module.children)
            for child in curr_module.children:
                # print(curr_module.name, f'-{pulse}->', child)
                if child not in modules:
                    continue  # most likely a sink
                child = modules[child]
                if child.module_type == '%':
                    if not pulse:
                        module_states[child.name] = not module_states[child.name]
                        process_buffer.append((child, module_states[child.name]))

                elif child.module_type == '&':
                    # if curr_module.name not in module_predecessors[child.name]:
                    #    raise Exception(f'Predecessor {curr_module.name} not found in {child.name}')
                    module_predecessors[child.name][curr_module.name] = pulse
                    if all(module_predecessors[child.name].values()):  # if last signal from all predecessors is True
                        process_buffer.append((child, False))
                    else:
                        process_buffer.append((child, True))
        # print(module_states)
    print(cnt)
    return cnt[True] * cnt[False]


def part_2(part_input):
    part_input = part_input.strip().split('\n')
    modules = parse_modules(part_input)
    process_buffer = []
    cnt = {True: 0, False: 0}

    module_states = {m: False for m in modules}
    module_predecessors = {m: {} for m in modules}

    for key, value in modules.items():
        for c in value.children:
            if c not in module_predecessors:
                module_predecessors[c] = {}
            module_predecessors[c][key] = False

    print(modules)
    print('-' * 32)
    print(module_predecessors)
    print('-' * 32)
    print(module_states)
    print('-' * 32)
    idx = 0
    while True:
        idx += 1
        # print(idx)
        # print(module_states)
        cnt[False] += 1
        process_buffer = [(modules['broadcaster'], False)]
        while len(process_buffer):
            curr_module, pulse = process_buffer.pop(0)
            cnt[pulse] += len(curr_module.children)
            for child in curr_module.children:
                # print(curr_module.name, f'-{pulse}->', child)
                if child == 'rx' and not pulse:
                    return idx
                if child not in modules:
                    continue  # most likely a sink
                child = modules[child]
                if child.module_type == '%':
                    if not pulse:
                        module_states[child.name] = not module_states[child.name]
                        process_buffer.append((child, module_states[child.name]))

                elif child.module_type == '&':
                    # if curr_module.name not in module_predecessors[child.name]:
                    #    raise Exception(f'Predecessor {curr_module.name} not found in {child.name}')
                    module_predecessors[child.name][curr_module.name] = pulse
                    if all(module_predecessors[child.name].values()):  # if last signal from all predecessors is True
                        process_buffer.append((child, False))
                    else:
                        process_buffer.append((child, True))
        # print(module_states)
    print(cnt)
    return cnt[True] * cnt[False]


if __name__ == '__main__':
    puzzle_input = aoc_helpers.get_puzzle_input(year=YEAR, day=DAY, readlines=False)

    if not SKIP_1:
        for test_case, solution in TEST_CASES_1:
            test_result = part_1(test_case)
            assert test_result == solution, f'{test_result} != {solution}'
        res_1 = part_1(puzzle_input)
        print('Solution for part 1 is: ', res_1)
        # aoc_helpers.post_answer(res_1, DAY, 1, year=YEAR)

    # for test_case, solution in TEST_CASES_2:
    #    test_result = part_2(test_case)
    #    # assert test_result == solution, f'{test_result} != {solution}'

    res_2 = part_2(puzzle_input)
    print('Solution for part 2 is: ', res_2)
    # aoc_helpers.post_answer(res_2, DAY, 2, year=YEAR)
