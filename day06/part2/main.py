
input = [line.strip() for line in open("input.txt").readlines()]

s = set()
total = 0
new_group = True

for line in input:
    if len(line) == 0:
        total += len(s)
        s = set()
        new_group = True
    else:
        if new_group:
            for c in line:
                s.add(c)
            new_group = False
        else:
            temp = set()
            for c in s:
                if c in line:
                    temp.add(c)
            s = temp

total += len(s)
print(total)

exit()