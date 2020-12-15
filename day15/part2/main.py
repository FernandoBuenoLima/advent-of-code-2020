input = "6,3,15,13,1,0"

sequence = [int(n) for n in input.split(',')]

d = dict()

for i in range(len(sequence)):
    n = sequence[i]
    d[n] = i+1

current_position = len(sequence)
next_number = 0

while current_position < 30000000:
    current_number = next_number
    current_position += 1
    
    if current_number in d:
        next_number = current_position - d[current_number]
    else:
        next_number = 0
    d[current_number] = current_position

print(current_number)
exit()