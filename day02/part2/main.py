
def count_letter_matches(line):
    ret = 0
    
    password = line[3]
    pos1 = line[0]-1
    pos2 = line[1]-1
    letter = line[2]
    
    if password[pos1] == letter:
        ret += 1
    if password[pos2] == letter:
        ret += 1
    
    return ret


inputs = []

for line in open("input.txt").readlines():
    policy, password = line.split(':')
    range_string, letter = policy.strip().split(' ')
    lower_b, upper_b = range_string.split('-')
    
    inputs.append([int(lower_b), int(upper_b), letter, password.strip()])
    
c = 0
    
for i in inputs:
    if count_letter_matches(i) == 1:
        c += 1
        
print(c)