
file_path = ("input1.txt")

data = list()

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()

        if ':' in line:
            solution_str, values_str = line.split(':')
            solution = int(solution_str.strip())
            values = list(map(int, values_str.split()))
            data.append((solution, values))

def solve(answer, current_value, line_data, data_idx, concat):
    if current_value == answer and data_idx == len(line_data) : return True
    if current_value > answer:
        return False
    if data_idx == len(line_data):
        return False

    multiplied = current_value * line_data[data_idx]
    if solve(answer, multiplied, line_data, data_idx + 1, concat):
        return True

    added = current_value + line_data[data_idx]
    if solve(answer, added, line_data, data_idx + 1, concat):
        return True

    if concat:
        concatenated = int(str(current_value) + str( line_data[data_idx]))
        if solve(answer, concatenated, line_data, data_idx + 1, concat):
            return True

    return False

result = 0
for solution, values in data:
    if solve(solution, values[0], values, 1, False):
        result = result + solution


print('Answer1: '+str(result))
result = 0

for solution, values in data:
    if solve(solution, values[0], values, 1, True):
        print()
        result = result + solution

print('Answer2: ' + str(result))