
def find_sum_of_2(preamble, number):
    for i in range(len(preamble) - 1):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False

def find_target(input):
    for i in range(25, len(input)):
        number = input[i]
        preamble = input[i-25:i]
        if not find_sum_of_2(preamble, number):
            return number

input = [int(line.strip()) for line in open("input.txt").readlines()]

target = find_target(input)

i = 0
j = 1

while j < len(input):
    current_array = input[i:j+1]
    s = sum(current_array)
    if s == target:
        print(min(current_array) + max(current_array))
        exit()
    elif s < target:
        j += 1
    else: #s > target
        i += 1
        if i == j:
            j += 1

print("not found")
exit()
