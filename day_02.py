import re


def read_input(file='input.txt'):
    input_data = []
    with open(file, 'r') as input_file:
        for line in input_file:
            m = re.search('(\d+)\s*-\s*(\d+)\s*(\w)\s*:\s*(\w+)', line)
            lowest, highest, char, password = m.groups()
            input_data.append({
                'l': int(lowest),
                'h': int(highest),
                'c': char,
                'p': password,
            })
    return input_data


data = read_input()


def validate_password_01(lowest: int, highest: int, char: str, password: str):
    n = password.count(char)
    if n < lowest or n > highest:
        return 0
    else:
        return 1


def process_input_01(data):
    n = 0
    for e in data:
        n += validate_password_01(e['l'], e['h'], e['c'], e['p'])
    return n


def validate_password_02(first_entry, second_entry, char, password):
    a = password[first_entry - 1]
    b = password[second_entry - 1]
    if (a == char and b != char) or (a != char and b == char):
        return 1
    return 0


def process_input_02(data):
    n = 0
    for e in data:
        n += validate_password_02(e['l'], e['h'], e['c'], e['p'])
    return n


n = process_input_02(data)
print(n)
