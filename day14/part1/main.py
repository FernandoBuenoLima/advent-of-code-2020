
inputs = [line.strip() for line in open("input.txt").readlines()]
memory = dict()

for command in inputs:
    if command.startswith("mask"):
        mask = command[7:]
        or_mask = int(mask.replace('X', '0'), 2)
        and_mask = int(mask.replace('X', '1'), 2)
    elif command.startswith("mem"):
        address = int(command[4:command.index("]")])
        value = int(command[command.index("=")+2:])
        memory[address] = value & and_mask | or_mask
    else:
        print("Unrecognized command: '", command, "'")
        exit()

total = 0
for addr in memory:
    total += memory[addr]
print(total)

exit()
