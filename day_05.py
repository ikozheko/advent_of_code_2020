def binary_part(start, end, part_type):
    start_of_upper = (start + end + 1) // 2
    if part_type == 'LOWER':
        return start, start_of_upper - 1
    elif part_type == 'UPPER':
        return start_of_upper, end


def binary_partitioning(seat_descriptor):
    row_start = 0
    row_end = 127
    column_start = 0
    column_end = 7
    row = None
    column = None
    for c in seat_descriptor:
        # row lower half
        if c == 'F':
            row_start, row_end = binary_part(row_start, row_end, 'LOWER')
        # row upper half
        elif c == 'B':
            row_start, row_end = binary_part(row_start, row_end, 'UPPER')
        if row_start == row_end:
            row = row_start

        # column lower half
        if c == 'L':
            column_start, column_end = binary_part(column_start, column_end, 'LOWER')
        # column upper half
        elif c == 'R':
            column_start, column_end = binary_part(column_start, column_end, 'UPPER')
        if column_start == column_end:
            column = column_start
    return row, column


def get_seat_id(row, column):
    return row * 8 + column


def seat_id_generator():
    with open('input.txt', 'r') as f:
        for line in f:
            if line == '\n':
                break
            descriptor = line.strip()
            r, c = binary_partitioning(descriptor)
            yield get_seat_id(r, c)


existing_ids = []
min_id = None
max_id = 0
for seat_id in seat_id_generator():
    min_id = seat_id if min_id is None else min(min_id, seat_id)
    max_id = max(max_id, seat_id)
    existing_ids.append(seat_id)


print('max_id =', max_id)
for i in range(min_id, max_id + 1):
    if i not in existing_ids:
        print('missed_id =', i)
        break
