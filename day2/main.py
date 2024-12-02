import numpy as np

file_path = "./input1.txt"

data = []
with open(file_path, "r") as f:
    for line in f:
        row = list(map(int, line.split()))
        row += [np.nan] * (8 - len(row))
        data.append(row)

data = np.array(data)

def is_sorted(row):
    valid = ~np.isnan(row)
    row = row[valid]
    if len(row) <= 1:
        return True
    is_sorted_asc = np.all(row[:-1] <= row[1:])
    is_sorted_desc = np.all(row[:-1] >= row[1:])
    max_diff = np.all(np.abs(row[:-1] - row[1:]) <= 3)
    no_duplicates = np.all(row[:-1] != row[1:])
    return (is_sorted_asc or is_sorted_desc) and max_diff and no_duplicates

sorted = np.array([is_sorted(row) for row in data])
print('Answer 1: ' + str(np.sum(sorted)))

def is_sorted_one_off(row):
    if is_sorted(row):
        return True

    valid = ~np.isnan(row)
    row = row[valid]
    for i, _ in enumerate(row):
        clone = row.copy()
        clone = np.delete(clone, i )
        if is_sorted(clone):
            return True

    return False

sorted = np.array([is_sorted_one_off(row) for row in data])

print('Answer 2: ' + str(np.sum(sorted)))
