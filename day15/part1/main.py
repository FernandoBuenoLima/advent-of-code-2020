def add_next_number(sequence):
    last = sequence[0]
    if not last in sequence[1:]:
        sequence.insert(0, 0)
    else:
        i = sequence.index(last, 1)
        sequence.insert(0, i)

input = "6,3,15,13,1,0"

sequence = [int(n) for n in input.split(',')]
sequence = sequence[::-1]

while len(sequence) < 2020: add_next_number(sequence)

print(sequence[0])
exit()