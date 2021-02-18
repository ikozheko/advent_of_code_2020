def read_map(file='input.txt'):
    m = []
    with open(file, 'r') as input_file:
        for line in input_file:
            line = line.replace('\n', '')
            m.append([c for c in line])
    return m


m = read_map()
map_width, map_height = len(m[0]), len(m)


def move(from_x, from_y, delta_x, delta_y):
    global map_width
    to_x = (from_x + delta_x) % map_width
    to_y = (from_y + delta_y)
    return to_x, to_y


def run(delta_x, delta_y):
    count_of_trees = 0
    move_is_finished = False
    x = y = 0

    while not move_is_finished:
        x, y = move(x, y, delta_x, delta_y)
        if m[y][x] == '#':
            count_of_trees += 1
        if y == map_height - 1:
            break
    return count_of_trees


n = run(1, 1) * run(3, 1) * run(5, 1) * run(7, 1) * run(1, 2)
print(n)
