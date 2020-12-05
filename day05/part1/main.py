
def getLowerHalf(range):
    newUpperBound = (range[0] + range[1] - 1) / 2
    range[1] = int(newUpperBound)

def getUpperHalf(range):
    newLowerBound = (range[0] + range[1] + 1) / 2
    range[0] = int(newLowerBound)

def getSeatRow(data):
    range = [0, 127]
    for c in data:
        if c == 'F':
            getLowerHalf(range)
        else:
            getUpperHalf(range)
    return range[0]

def getSeatColumn(data):
    range = [0, 7]
    for c in data:
        if c == 'L':
            getLowerHalf(range)
        else:
            getUpperHalf(range)
    return range[0]

def getSeatId(data):
    row = getSeatRow(data[:7])
    column = getSeatColumn(data[7:])
    return (row * 8) + column

ids = [getSeatId(line.strip()) for line in open("input.txt").readlines()]
print(max(ids))
exit()