
entries = [int(l) for l in open("input.txt").readlines()]
target_sum = 2020

for i in range(len(entries) - 1):
    for j in range(i+1, len(entries)):
        if entries[i] + entries[j] == target_sum:
            print(entries[i] * entries[j])
            exit()
