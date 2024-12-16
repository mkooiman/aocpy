file_path = "input1.txt"
ordering = []
pageOrdering = []
with open(file_path, 'r') as file:
    for line in file:
        if line == "\n":
            break
        ordering.append(line.strip())
    for line in file:
        pageOrdering.append(line.strip().split(','))

max = max(len(row) for row in pageOrdering)


invalidRows = list()

def processRow(row):
    pairs = list(zip(row[:-1], row[1:]))
    valid = True
    itemNr = 0
    for combo in pairs:
        if str(combo[0]) + '|' + str(combo[1]) not in ordering and combo[0] != 0 and combo[1] != 0:
            valid = False
            tmp = row[itemNr]
            row[itemNr] = row[itemNr+1]
            row[itemNr+1] = tmp
            _, returnValue = processRow(row)
            return valid, returnValue

        itemNr += 1

    return valid, int(row[len(row) // 2])

theSumValid = 0
theSumInvalid = 0

for row in pageOrdering:
    valid, value = processRow(row)
    if valid:
        theSumValid += value
    else:
        theSumInvalid += value



print( 'answer 1: ' + str(theSumValid))
print( 'answer 2: ' + str(theSumInvalid))

