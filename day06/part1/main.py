
input = [line.strip() for line in open("input.txt").readlines()]

s = set()
total = 0

for line in input:
    if len(line) == 0:
        total += len(s)
        s = set()
    else:
        for c in line:
            s.add(c)

total += len(s)
print(total)

exit()