from itertools import combinations


def read_input(file='input.txt'):
    values = []
    with open(file, 'r') as input_file:
        for line in input_file:
            value = int(line)
            values.append(value)
    return values


def process_input_01(values):
    for i in range(1, len(values)):
        for j in range(0, i):
            if values[i] + values[j] == 2020:
                return values[i] * values[j]


def process_input_02(values):
    l = len(values)
    if l < 3:
        raise ValueError

    for i in combinations(values, 3):
        a, b, c = i
        if a + b + c == 2020:
            return a * b * c


values = read_input()
result = process_input_02(values)
if result is not None:
    print(f'result = {result}')
else:
    print(f'the solving is not found')
