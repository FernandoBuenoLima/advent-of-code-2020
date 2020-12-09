
def find_sum_of_2(preamble, number):
    for i in range(len(preamble) - 1):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False

input = [int(line.strip()) for line in open("input.txt").readlines()]

for i in range(25, len(input)):
    number = input[i]
    preamble = input[i-25:i]
    if not find_sum_of_2(preamble, number):
        print(number)
        exit()
    
print("not found")
exit()