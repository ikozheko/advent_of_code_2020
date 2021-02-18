def normalize_input(data):
    while data[0] == '':
        del data[0]
    while data[len(data) - 1] == '':
        del data[len(data) - 1]

    for i in range(0, len(data) - 1):
        if i < len(data) - 1:
            while data[i] == '' and data[i + 1] == '':
                del data[i]
    return data


def read_group(data, start_from):
    i = start_from
    group = []
    while i < len(data) and data[i] != '':
        group.append(data[i])
        i += 1
    if i < len(data) - 1:
        return i + 1, group
    else:
        return None, group


def group_generator():
    data = [i.strip() for i in open('input.txt', 'r')]
    data = normalize_input(data)
    start_from = 0
    while start_from is not None:
        start_from, grp = read_group(data, start_from)
        yield grp


def distinct_answers(group):
    s = set()
    for answers in group:
        for answer in answers:
            s.add(answer)
    return list(s)


def is_everyone_yes(group, answer):
    for answers in group:
        if not answer in answers:
            return False
    return True


def cartinality(group, criterion):
    n = 0
    for answer in distinct_answers(group):
        if criterion(group, answer):
            n += 1
    return n


n = 0
for group in group_generator():
    n += cartinality(group, is_everyone_yes)
print(n)
