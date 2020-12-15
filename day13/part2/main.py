from math import ceil
from bus import Bus

inputs = [bus.strip() for bus in open("input.txt").read().split(',')]

busses = []

for i in range(len(inputs)):
    if inputs[i] != 'x':
        busses.append(Bus(int(inputs[i]), i))

base = base_inc = busses[0].id
del busses[0]

while len(busses) > 0:
    if busses[0].check(base):
        base_inc *= busses[0].id
        del busses[0]
        continue
    base += base_inc

print(base)
exit()