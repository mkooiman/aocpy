import re
import numpy as np


file_path = "input1.txt"

file = ''
with open(file_path, "r") as f:
    for line in f:
        file = file + line

result = re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", file)
data = np.array(result, dtype=int)
data = np.multiply(data[:,0], data[:,1])
result = np.sum(data)
print('Answer 1: ' + str(result))

result = re.findall("((do\(\))|(don't\(\))|(mul\(([0-9]{1,3}),([0-9]{1,3})\)))", file)


enabled = True
answer = 0;
for match in result:
    if match[2]:
        enabled = False
    elif match[1]:
        enabled = True
    elif (match[3]!="")  & enabled:
        answer += int(match[4])* int(match[5])

print(answer)