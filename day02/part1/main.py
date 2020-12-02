
inputs = []

for line in open("input.txt").readlines():
    policy, password = line.split(':')
    range_string, letter = policy.strip().split(' ')
    lower_b, upper_b = range_string.split('-')
    
    inputs.append([int(lower_b), int(upper_b), letter, password.strip()])
    
c = 0
    
for i in inputs:
    count = i[3].count(i[2])
    if count >= i[0] and count <= i[1]:
        c += 1
        
print(c)