import aoc_helpers

YEAR = 2023
DAY = 19
SKIP_1 = False

TEST_CASES_1 = [
    (
        """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
""",
        19114,
    )
]
TEST_CASES_2 = [(TEST_CASES_1[0][0], 167409079868000)]
import functools


def smaller(val, target):
    return val < target


def greater(val, target):
    return val > target


def is_true(val):
    return True


def parse_rules(rules):
    ret = {}
    for rule in rules.strip().split('\n'):
        # print(rule)
        name, rest = rule.split('{')
        ret[name] = {}
        c = []
        conditions = rest[:-1].split(',')
        for cond in conditions:
            if '<' in cond:
                inval, check = cond.split('<')
                checkval, target = check.split(':')
                c.append(
                    {
                        'check': functools.partial(smaller, target=int(checkval)),
                        'input': inval,
                        'target': target,
                        'cond': '<',
                        'val': int(checkval),
                    }
                )
            elif '>' in cond:
                inval, check = cond.split('>')
                checkval, target = check.split(':')
                c.append(
                    {
                        'check': functools.partial(greater, target=int(checkval)),
                        'input': inval,
                        'target': target,
                        'cond': '<',
                        'val': int(checkval),
                    }
                )
            else:
                c.append({'check': functools.partial(is_true), 'input': 'x', 'target': cond, 'cond': '', 'val': ''})
        ret[name]['checks'] = c
    return ret


def parse_parts(parts):
    ret = []
    for part in parts.strip().split('\n'):
        x, m, a, s = part[:-1].split(',')
        x = int(x.split('=')[-1])
        m = int(m.split('=')[-1])
        a = int(a.split('=')[-1])
        s = int(s.split('=')[-1])
        ret.append({'x': x, 'm': m, 'a': a, 's': s})
    return ret


def part_1(part_input):
    rules, parts = part_input.strip().split('\n\n')
    ruleset = parse_rules(rules)
    partslist = parse_parts(parts)

    accepted = 0
    for part in partslist:
        finished = False
        curr_rule = ruleset['in']
        check_idx = 0
        while not finished:
            check = curr_rule['checks'][check_idx]
            if check['check'](part[check['input']]):
                curr_rule = check['target']
                check_idx = 0
                if curr_rule == 'A':
                    accepted += part['x'] + part['m'] + part['a'] + part['s']
                    finished = True
                    break
                elif curr_rule == 'R':
                    finished = True
                    break
                curr_rule = ruleset[curr_rule]

            else:
                check_idx += 1

    return accepted


def part_2(part_input):
    rules, parts = part_input.strip().split('\n\n')
    ruleset = parse_rules(rules)
    # partslist = parse_parts(parts)    # figure out which parts will be accepted in advance
    # each xmas val can be  1 to a maximum of 4000
    ranged_part = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    to_process = [('in', 0, ranged_part)]
    accepted = []

    while len(to_process):
        curr_rule, rule_idx, part = to_process.pop(0)
        # print(part)

        if curr_rule == 'A':
            accepted.append(part)
            break
        elif curr_rule == 'R':
            print('REJECTED!')
            break

        rule = ruleset[curr_rule]['checks'][rule_idx]
        vmin, vmax = part[rule['input']]

        if rule['cond'] == '<':
            if vmin <= rule['val'] - 1:
                tmp = part.copy()
                tmp[rule['input']] = (vmin, rule['val'] - 1)
                to_process.append((curr_rule, rule_idx + 1, tmp))

            if rule['val'] <= vmax:
                tmp = part.copy()
                tmp[rule['input']] = (rule['val'], vmax)
                to_process.append((rule['target'], 0, tmp))  # rule_idx

        elif rule['cond'] == '>':
            if rule['val'] <= vmax:
                tmp = part.copy()
                tmp[rule['input']] = (rule['val'], vmax)
                to_process.append((curr_rule, rule_idx + 1, tmp))

            if vmin <= rule['val'] - 1:
                tmp = part.copy()
                tmp[rule['input']] = (vmin, rule['val'] - 1)
                to_process.append((rule['target'], 0, tmp))  # rule_idx

        elif rule['cond'] == '':
            tmp = part.copy()
            to_process.append((rule['target'], 0, tmp))

    print(accepted)
    return 'not solved'


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
