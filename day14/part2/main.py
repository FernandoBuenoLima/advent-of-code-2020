
def replaceat(s, index, new_value):
    return s[:index] + new_value + s[index+1:]

def get_all_fixed_masks(mask):
    and_mask = mask.replace('0', '1')
    masks = [[and_mask, mask]]
    while 'X' in masks[0][0]:
        new_masks = []
        i = masks[0][0].index('X')
        for m in masks:
            new_masks.append([replaceat(m[0], i, '0'), replaceat(m[1], i, '0')])
            new_masks.append([replaceat(m[0], i, '1'), replaceat(m[1], i, '1')])
        masks = new_masks
    return masks

inputs = [line.strip() for line in open("input.txt").readlines()]
memory = dict()

for command in inputs:
    if command.startswith("mask"):
        masks = get_all_fixed_masks(command[7:])
    elif command.startswith("mem"):
        address = int(command[4:command.index("]")])
        value = int(command[command.index("=")+2:])
        for m in masks:
            masked_address = address & int(m[0], 2) | int(m[1], 2)
            memory[masked_address] = value

total = 0
for addr in memory:
    total += memory[addr]
print(total)

exit()
