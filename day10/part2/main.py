
def is_possibility(array):
    for i in range(len(array)-1):
        if array[i+1]-array[i] > 3:
            return False
    return True

def count_possibilities(array):
    candidates = [[array[0]]]
    
    for i in range(1, len(array)-1):
        item = array[i]
        new_candidates = []
        for c in candidates:
            new_c = c.copy()
            new_c.append(item)
            new_candidates.append(new_c)
        candidates.extend(new_candidates)
    
    total = 0
    
    for c in candidates:
        c.append(array[-1])
        if is_possibility(c):
            total += 1
    
    return total


input = [int(line.strip()) for line in open("input.txt").readlines()]
input.append(0)
input.sort()

array_started = False
array_start = -1
total = 1

for i in range(len(input)-1):
    if input[i+1] - input[i] == 1:
        if not array_started:
            array_start = i
            array_started = True
    else:
        if array_started:
            array = input[array_start:i+1]
            if len(array) >= 3:
                total *= count_possibilities(array)
            array_started = False

if array_started:
    total *= count_possibilities(input[array_start:])

print(total)
exit()
