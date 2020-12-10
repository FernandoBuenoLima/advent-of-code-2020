
input = [int(line.strip()) for line in open("input.txt").readlines()]
input.sort()

gaps = [0, 0, 1]

level = 0

for adapter in input:
    gaps[adapter-level-1] += 1
    level = adapter
    
print(gaps[0]*gaps[2])
exit()
