import re
import pprint


def rule_generator():
    for line in open('input.txt', 'r'):
        yield parse_rule(line)


def parse_inner(inner):
    inner = str(inner).strip()
    if inner.endswith('no other bags.'):
        return []
    m = re.search(r'^(\d+)(.+)bag', inner)
    count, bag_type = m.groups()
    return {
        'count': int(count),
        'type': bag_type.strip(),
    }


def parse_rule(rule):
    outer, inners = rule.split('bags contain')
    inners = inners.strip()
    outer = outer.strip()
    obj = []
    if ',' in inners:
        inners = inners.split(',')
        for inner in inners:
            obj.append(parse_inner(inner))
    else:
        obj = parse_inner(inners)
    return {
        outer: obj
    }


def can_contain_shiny_gold(rules, current_bag_type):
    for rule in rules:
        key = list(rule.keys())[0]
        if key == current_bag_type:
            return False
        nested_bags = rule[key]
        print('-------------------------')
        print(key)
        for bag in nested_bags:
            print(f'\t{bag}')
            if bag['count'] <= 0:
                continue
            elif current_bag_type == bag['type']:
                return True
            else:
                return can_contain_shiny_gold(rules, bag['type'])


def main():
    rules = []
    for i, rule in enumerate(rule_generator()):
        rules.append(rule)

    # printer = pprint.PrettyPrinter(indent=4)
    # printer.pprint(rules)

    bag_type_for_search = 'shiny gold'
    n = 0
    for rule in rules:
        n += 1 if can_contain_shiny_gold(rules, bag_type_for_search) else 0
    print(n)


if __name__ == '__main__':
    main()
