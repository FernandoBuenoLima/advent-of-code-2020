
entries = [int(l) for l in open("input.txt").readlines()]
target_sum = 2020

for i in range(len(entries)-2):
    for j in range(i+1, len(entries)-1):
        for k in range(j+1, len(entries)):
            if entries[i] + entries[j] + entries[k] == target_sum:
                print(entries[i] * entries[j] * entries[k])
                exit()
